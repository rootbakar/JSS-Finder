# Skrip Python untuk memproses file list-js.txt

def extract_links(input_file, output_file):
    try:
        # Buka file input untuk dibaca
        with open(input_file, 'r') as infile:
            lines = infile.readlines()

        # Ekstraksi link valid
        links = []
        for line in lines:
            if line.startswith('[+] Valid URL found:'):
                link = line.split(':', 1)[1].strip()
                links.append(link)

        # Simpan hasil ke file output
        with open(output_file, 'w') as outfile:
            outfile.write('\n'.join(links))

        print(f"Successfully extracted {len(links)} links to {output_file}")
    except FileNotFoundError:
        print(f"Error: File {input_file} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Nama file input dan output
input_file = 'list-js.txt'  # Ganti dengan nama file Anda
output_file = 'extracted-links.txt'  # Nama file hasil output

# Jalankan fungsi ekstraksi
extract_links(input_file, output_file)
