import os

def rename_files_and_folders(directory):
    # Get a list of all files and folders in the specified directory
    for name in os.listdir(directory):
        # Construct the full path
        old_path = os.path.join(directory, name)
        
        # Replace dashes with spaces in the name
        new_name = name.replace("-", " ")
        new_path = os.path.join(directory, new_name)
        
        # Rename the file or folder
        if old_path != new_path:  # Avoid renaming if the name hasn't changed
            os.rename(old_path, new_path)
            print(f'Renamed: {old_path} -> {new_path}')

if __name__ == "__main__":
    # Get the directory where the script is located
    script_directory = os.path.dirname(os.path.abspath(__file__))
    
    # Rename files and folders in the script's directory
    rename_files_and_folders(script_directory)