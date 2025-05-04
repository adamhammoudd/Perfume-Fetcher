# Perfume Fetcher

Perfume-Fetcher is a Python-based application designed to help users search for fragrances based on their favorite notes in a perfume.

## Features

- **Search Functionality**: Filter perfumes based on user preferences such as fragrance notes, gender, and minimum rating.
- **Note Match Scoring**: Calculates a score (0-5) based on how well the perfume's notes match the user's preferred notes.
- **User-Friendly Output**: Displays the top 5 perfume recommendations in a tabular format.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/adamhamoudd/Perfume-Fetcher.git
    ```
2. Navigate to the project directory:
    ```bash
    cd Perfume-Fetcher
    ```
3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

Run the application using the following command:
```bash
python main.py
```
Follow the on-screen instructions to search for perfumes and view detailed information.

### Example Usage
```text
Enter your preferred notes (comma-separated): woody, musky, mineral
For which gender: for men
Enter your minimum rating (0-5): 3

Top 5 Perfume Recommendations:

╒═════════════════════════════════════╤═════════╤════════════════════╕
│ Perfume Name                        │ Rating  │ Note Match Score   │
╞═════════════════════════════════════╪═════════╪════════════════════╡
│ Valentino Uomo Born in Roma         │ 4.23    │ 5.0                │
│ The Collection Bold Incense         │ 4.00    │ 4.0                │
│ XXX Verdigris Ermenegildo Zegna     │ 4.00    │ 3.5                │
│ Hype for Him Hinode                 │ 4.22    │ 3.0                │
│ Majestic Oud Afnan                  │ 3.83    │ 2.5                │
╘═════════════════════════════════════╧═════════╧════════════════════╛
```
## How It Works

**User Input:**
- Enter your preferred fragrance notes (e.g., woody, musky, mineral).
- Specify the gender (for men or for women).
- Provide a minimum rating (e.g., 3).

### Filtering:
- The program filters perfumes based on the specified gender and minimum rating.

### Note Match Scoring:
- Each perfume is scored based on how many of the user's preferred notes are present in the perfume's Main Accords.
- The score is normalized to a range of 0-5.

### Output:
- The top 5 perfumes are displayed in a table, sorted by the Note Match Score.

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests to improve the project.

## License

This project is licensed under the MIT License.

## Acknowledgments

Thanks to the open-source community for providing tools and libraries that made this project possible.
Special thanks to fragrance enthusiasts for inspiring this idea.
