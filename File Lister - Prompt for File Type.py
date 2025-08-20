import os
import tkinter as tk
from tkinter import simpledialog, messagebox

def list_files_by_extension():
    # Create a Tkinter root window (hidden)
    root = tk.Tk()
    root.withdraw()

    # Prompt user for file extensions
    user_input = simpledialog.askstring(
        title="File Type Input",
        prompt="Enter the file extensions you want to list (e.g., .mp3, .jpg, .csv):",
    )

    if not user_input:
        messagebox.showinfo("No Input", "No file types entered. Exiting the script.")
        return

    # Parse and clean the input
    extensions = [ext.strip() for ext in user_input.split(",") if ext.strip()]

    # Get the directory where the script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # List all files in the directory matching the specified extensions
    files = [file for file in os.listdir(script_dir) if any(file.endswith(ext) for ext in extensions)]

    # Prepare the output file path
    output_file_path = os.path.join(script_dir, 'List of Files.txt')

    # Write the list of file names (without extension) to the output file
    with open(output_file_path, 'w') as output_file:
        for file_name in files:
            output_file.write(file_name + '\n')

    # Inform the user
    messagebox.showinfo("Operation Complete", f"List of files saved to: {output_file_path}")

if __name__ == "__main__":
    list_files_by_extension()
