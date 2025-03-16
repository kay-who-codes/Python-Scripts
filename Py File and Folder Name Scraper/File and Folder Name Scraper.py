import os
import sys

def get_parent_folder():
    """Retrieve the parent folder name of the script."""
    return os.path.basename(os.path.dirname(os.path.abspath(__file__)))

def list_files_and_folders(base_path, format_option):
    """List all files and folders including subfolders."""
    structure = []
    for root, dirs, files in os.walk(base_path):
        if format_option == 'full_path':
            structure.append(f"Folder: {root}")
            structure.extend([f"  File: {os.path.join(root, file)}" for file in files])
        elif format_option == 'names_with_ext':
            structure.append(f"Folder: {os.path.basename(root)}")
            structure.extend([f"  File: {file}" for file in files])
        elif format_option == 'names_no_ext':
            structure.append(f"Folder: {os.path.basename(root)}")
            structure.extend([f"  File: {os.path.splitext(file)[0]}" for file in files])
    return structure

def list_folders_and_subfolders(base_path, format_option):
    """List only folders and subfolders."""
    structure = []
    for root, dirs, _ in os.walk(base_path):
        if format_option == 'full_path':
            structure.append(f"Folder: {root}")
        else:
            structure.append(f"Folder: {os.path.basename(root)}")
    return structure

def list_files_only(base_path, format_option):
    """List only files (no folders)."""
    structure = []
    for root, _, files in os.walk(base_path):
        if format_option == 'full_path':
            structure.extend([f"File: {os.path.join(root, file)}" for file in files])
        elif format_option == 'names_with_ext':
            structure.extend([f"File: {file}" for file in files])
        elif format_option == 'names_no_ext':
            structure.extend([f"File: {os.path.splitext(file)[0]}" for file in files])
    return structure

def save_to_file(content, filename):
    """Save content to a file in the same directory as the script."""
    script_dir = os.path.dirname(os.path.abspath(__file__))  # Get the script's directory
    output_path = os.path.join(script_dir, filename)  # Combine script directory with filename
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(content))

def display_menu():
    """Display a menu to the user and get their selection."""
    print("\nChoose an option:")
    print("1. All Files, Folders, and Subfolders")
    print("2. All Folders and Subfolders (no files)")
    print("3. All Files (no folders)")
    print("\nChoose output format:")
    print("a. Full paths")
    print("b. Names only (with extensions)")
    print("c. Names only (without extensions)")

    choice = input("Enter your choice (1/2/3): ").strip()
    format_option = input("Enter format option (a/b/c): ").strip()

    if choice not in ('1', '2', '3') or format_option not in ('a', 'b', 'c'):
        print("Invalid selection. Please try again.")
        sys.exit(1)

    format_map = {'a': 'full_path', 'b': 'names_with_ext', 'c': 'names_no_ext'}
    return choice, format_map[format_option]

if __name__ == "__main__":
    # Get the parent folder name and path
    parent_folder = get_parent_folder()
    parent_path = os.path.dirname(os.path.abspath(__file__))

    # Display menu and get user input
    choice, format_option = display_menu()

    # Process choice
    if choice == '1':
        output = list_files_and_folders(parent_path, format_option)
    elif choice == '2':
        output = list_folders_and_subfolders(parent_path, format_option)
    elif choice == '3':
        output = list_files_only(parent_path, format_option)

    # Prepare the output file name and save
    output_filename = f"File Names - {parent_folder}.txt"
    save_to_file(output, output_filename)

    print(f"\nList saved to '{output_filename}'")
