import os
import re

def transform_filename(filename):
    # Define a more flexible regex pattern
    # This captures any character (including underscores, spaces, punctuation, etc.) in title and publisher
    pattern = r'^[^–]+ - (.+?) - (.+?) \((\d{4})\)\.[a-zA-Z0-9]+$'
    
    # Search for the pattern in the given filename
    match = re.match(pattern, filename)
    
    # If there's a match, format the filename as required
    if match:
        book_title = match.group(1).strip()
        publisher = match.group(2).strip()
        year = match.group(3)
        
        # Construct the new filename format, preserving the file extension
        new_filename = f"{book_title} - {publisher} ({year}){os.path.splitext(filename)[1]}"
        return new_filename
    
    # Return None if it doesn't match the expected format
    return None

def rename_files_in_folder(folder_path):
    # Loop through each file in the specified folder
    for filename in os.listdir(folder_path):
        # Only process files, ignore directories
        if os.path.isfile(os.path.join(folder_path, filename)):
            # Transform the filename according to the specified pattern
            new_filename = transform_filename(filename)
            
            # If transformation was successful and a new name was returned
            if new_filename:
                # Get full path for old and new filenames
                old_file = os.path.join(folder_path, filename)
                new_file = os.path.join(folder_path, new_filename)
                
                # Rename the file
                os.rename(old_file, new_file)
                print(f"Renamed: '{filename}' to '{new_filename}'")
            else:
                print(f"Skipped: '{filename}' (doesn't match expected format)")

# Specify the folder path
folder_path = r"C:\Users\Kay\Desktop\Books"
rename_files_in_folder(folder_path)
