import csv
import os

def tsv_to_csv(tsv_file_path, output_csv_file):
    """
    Convert TSV formatted file into CSV and write it to a file, ensuring proper UTF-8 encoding.

    Args:
        tsv_file_path (str): Path to the input TSV file.
        output_csv_file (str): File name for the CSV output.
    """
    # Read the TSV file with UTF-8 encoding
    with open(tsv_file_path, "r", encoding="utf-8") as tsv_file:
        rows = tsv_file.readlines()
    
    # Split each row into columns based on tab character
    data = [row.strip().split("\t") for row in rows]

    # Write the data to a CSV file with UTF-8 encoding
    with open(output_csv_file, "w", newline='', encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(data)

# Detect any .tsv files in the same folder
current_folder = os.getcwd()
ts_files = [f for f in os.listdir(current_folder) if f.endswith(".tsv")]

if not ts_files:
    print("No .tsv files found in the current folder.")
else:
    for tsv_file in ts_files:
        # Define output CSV file name
        output_file = os.path.join(current_folder, "NEW_CSV_FILE_FROM_TSV.csv")
        
        # Convert the first found TSV to CSV
        print(f"Converting {tsv_file} to {output_file}...")
        tsv_to_csv(os.path.join(current_folder, tsv_file), output_file)
        print(f"Conversion complete. Saved to {output_file}.")
        break  # Only process the first .tsv file
