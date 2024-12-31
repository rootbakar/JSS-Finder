def extract_links(input_file, output_file):
    try:
        with open(input_file, 'r') as infile:
            lines = infile.readlines()

        links = []
        for line in lines:
            if line.startswith('[+] Valid URL found:'):
                link = line.split(':', 1)[1].strip()
                links.append(link)

        with open(output_file, 'w') as outfile:
            outfile.write('\n'.join(links))

        print(f"Successfully extracted {len(links)} links to {output_file}")
    except FileNotFoundError:
        print(f"Error: File {input_file} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

input_file = 'list-js.txt'
output_file = 'extracted-links.txt'

# Jalankan fungsi ekstraksi
extract_links(input_file, output_file)
