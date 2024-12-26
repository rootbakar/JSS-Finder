# RB-JSS-Finder (JS String Finder)

**JS String Finder** is a useful tool for searching specific strings in JavaScript files fetched from a list of URLs. This tool can assist security researchers, developers, and analysts in identifying potential issues or exploring strings present in JS files hosted on various URLs.

## Features
- Fetches JS URLs from a file containing a list of JS links.
- Searches for specific strings within the JavaScript content fetched from each URL.
- Displays relevant search results in an easy-to-read format.
- Provides a progress bar to monitor the search process status.

## Installation

To run **JS String Finder**, make sure you have Python 3 installed along with the necessary dependencies. You can install them by running:

```bash
pip install requests beautifulsoup4 tqdm colorama pyfiglet --break-system-packages
```

# Usage

## Running the Tool
To use JS String Finder, run the Python script with the following options:

```bash
python3 js-string-finder.py -l <path_to_file_with_links> -s <comma_separated_strings_to_search>
```

## Options

- `-h, --help`: Show the help message and exit.
- `-l, --list LIST`: Path to the file containing JS links (e.g., `js-link.txt`).
- `-s, --strings STRINGS`: Comma-separated strings to search for (e.g., `keyword1,keyword2`).

# Example: Obtaining JS Links
You can combine JS String Finder with jsfinder to automatically fetch JavaScript links from a website. Run the following command to extract the links from a website and store them in a file called `js-link.txt`:

```bash
echo "https://example.com" | jsfinder -read -s -o js-link.txt
```

or 


```bash
echo "https://subs.example.com" | jsfinder -read -s -o js-link.txt
```

**Result:**

<img width="1440" alt="Screenshot 2024-12-26 at 09 26 04" src="https://github.com/user-attachments/assets/ef725a6f-a1a9-47ae-89a8-ceacaaeaa672" />


```bash
cat js-link.txt
```

**Result:**

<img width="788" alt="Screenshot 2024-12-26 at 09 22 57" src="https://github.com/user-attachments/assets/dd9d34a9-6e53-4d0d-b0c8-1a1d2cdac865" />


`First you must installed the jsfinder tools` https://github.com/kacakb/jsfinder


# Example: Searching for Strings
```bash
python3 js-string-finder.py -l js-link.txt -s "Admin"
```

**Result:**

<img width="1439" alt="Screenshot 2024-12-26 at 09 18 19" src="https://github.com/user-attachments/assets/e567c118-a7ba-49ef-88e6-80e9bcf989df" />


# Acknowledgement
This tools inspired by [jsfinder](https://github.com/kacakb/jsfinder)

