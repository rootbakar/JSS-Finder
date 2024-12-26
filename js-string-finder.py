import requests
import argparse
from urllib.parse import urljoin
from bs4 import BeautifulSoup
from tqdm import tqdm
from colorama import Fore, Style
import pyfiglet

# Fungsi untuk membaca file dan mencari string tertentu di file JS
def search_strings_in_js(file_with_links, strings_to_search):
    try:
        with open(file_with_links, 'r') as file:
            links = file.readlines()

        # Bersihkan link dari karakter newline
        links = [link.strip() for link in links if link.strip()]
        
        results = {}

        print(Fore.GREEN + "\n" + pyfiglet.figlet_format("RB-JSS-Finder", font="slant") + Style.RESET_ALL)
        print(Fore.GREEN + "Version 1\nStarting search...\n" + Style.RESET_ALL)
        
        for link in tqdm(links, desc="Processing JS links", colour="green"):
            try:
                response = requests.get(link, timeout=10)
                response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
                content = response.text

                matches = []
                for string in strings_to_search:
                    if string in content:
                        matches.append(string)

                if matches:
                    results[link] = matches

            except requests.RequestException as e:
                print(Fore.RED + f"Error fetching {link}: {e}" + Style.RESET_ALL)

        # Print hasil
        for link, matches in results.items():
            print(Fore.GREEN + f"\nIn {link}, found: {', '.join(matches)}" + Style.RESET_ALL)

        print(Fore.GREEN + "\nProcessing completed." + Style.RESET_ALL)

    except FileNotFoundError:
        print(Fore.RED + f"File {file_with_links} not found." + Style.RESET_ALL)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="JS String Finder Tool")
    parser.add_argument("-l", "--list", help="Path to file containing JS links", required=False)
    parser.add_argument("-s", "--strings", help="Comma-separated strings to search", required=False)

    args = parser.parse_args()

    if args.list and args.strings:
        strings_to_search = [s.strip() for s in args.strings.split(",") if s.strip()]
        search_strings_in_js(args.list, strings_to_search)

    elif not args.list:
        parser.print_help()

