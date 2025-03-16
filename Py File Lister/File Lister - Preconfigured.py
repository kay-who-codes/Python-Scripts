import os

def list_fst_files():
    # Get the directory where the script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # List all files in the directory with the '.fst' extension
    fst_files = [file for file in os.listdir(script_dir) if file.endswith('.FILE_EXTENSION_GOES_HERE')]

    # Prepare the output file path
    output_file_path = os.path.join(script_dir, 'List of Files.txt')

    # Write the list of .fst file names (without extension) to the output file
    with open(output_file_path, 'w') as output_file:
        for file_name in fst_files:
            output_file.write(os.path.splitext(file_name)[0] + '\n')

    print(f"List of .fst files saved to: {output_file_path}")

if __name__ == "__main__":
    list_fst_files()
