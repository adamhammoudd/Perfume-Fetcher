import pandas as pd
import ast
from tabulate import tabulate

# Load the dataset
df = pd.read_csv('perfumes.csv')

# Fix Main Accords column
df['Main Accords'] = df['Main Accords'].apply(lambda x: ast.literal_eval(x) if pd.notna(x) else [])

# Normalize gender column
df['Gender'] = df['Gender'].str.strip().str.lower()

# User input
user_notes = input("Enter your preferred notes (comma-separated): ").split(',')
user_notes = [note.strip().lower() for note in user_notes]
user_gender = input("For which gender: ").strip().lower()
user_min_rating = float(input("Enter your minimum rating (0-5): "))

# Matching function
def match_notes(row):
    row_notes = [note.lower() for note in row['Main Accords']]
    intersection = set(user_notes) & set(row_notes)
    return (len(intersection) / len(user_notes)) * 5 if user_notes else 0

# Filter by gender and rating
filtered = df[
    (df['Gender'] == user_gender) &
    (df['Rating Value'] >= user_min_rating)
].copy()

# Clean up 'Name' by removing 'for men' or 'for women'
filtered['Name'] = filtered['Name'].str.replace(r'\s*for men$', '', regex=True)
filtered['Name'] = filtered['Name'].str.replace(r'\s*for women$', '', regex=True)

# Add note match score
filtered['Note Match Score'] = filtered.apply(match_notes, axis=1)

# Sort and display top 5
top_5 = filtered.sort_values(by='Note Match Score', ascending=False).head(5)

# Format and display as a table
top_5_display = top_5[['Name', 'Rating Value', 'Note Match Score']].copy()
top_5_display.columns = ['Perfume Name', 'Rating', 'Note Match Score']
top_5_display = top_5_display.round(2)

print("\nTop 5 Perfume Recommendations:\n")
print(tabulate(top_5_display, headers='keys', tablefmt='fancy_grid', showindex=False))
