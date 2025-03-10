# Web Scraping Application

This project is a web scraping application that extracts news headlines from the Business Today technology news section and displays them in a Tkinter GUI.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)

- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/your-username/web-scraping.git
    cd web-scraping
    ```

2. Create and activate a virtual environment (optional but recommended):

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required dependencies:

    ```sh
    pip install -r requirements.txt
    ```

    If `requirements.txt` is not available, install the dependencies manually:

    ```sh
    pip install requests beautifulsoup4 tkinter
    ```

## Usage

1. Run the web scraping script:

    ```sh
    python Web\ Scraping.py
    ```

2. The Tkinter GUI will open, displaying the scraped news headlines.


- `Web Scraping.py`: The main script that performs web scraping and displays the results in a Tkinter GUI.
- `scraper.png`: The icon used for the Tkinter window.
- `Scrape.txt`: The file where the scraped news headlines are saved.
- `requirements.txt`: The file containing the list of dependencies.
- `README.md`: This file.


## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes.
