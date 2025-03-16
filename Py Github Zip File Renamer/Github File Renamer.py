import os
import datetime

# Function to format the datetime string
def format_datetime():
    now = datetime.datetime.now()
    # Round to the nearest hour
    rounded_hour = (now + datetime.timedelta(minutes=30)).replace(minute=0, second=0, microsecond=0)
    # Use `%#I` for Windows compatibility and make AM/PM lowercase
    return rounded_hour.strftime('%d %b, %Y %#I%p').lower()

# Function to reformat and rename files
def reformat_and_rename():
    # Get the current script's directory
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # List all files in the directory
    files = os.listdir(current_dir)

    # Filter files ending with "-main.zip"
    target_files = [f for f in files if f.endswith("-main.zip")]

    # Loop through the filtered files
    for file in target_files:
        # Remove "-main" and replace dashes with spaces
        new_name = file.replace("-main", f" - Downloaded from Github {format_datetime()}").replace("-", " ")

        # Add back a single dash before the date and ensure no extra spaces
        new_name = new_name.replace(" Downloaded from Github ", " - Downloaded from Github ")

        # Ensure that the first letter of the month is capitalised
        new_name = new_name.replace(new_name.split(" ")[2], new_name.split(" ")[2].capitalize())

        # Get the full paths
        old_path = os.path.join(current_dir, file)
        new_path = os.path.join(current_dir, new_name)

        # Rename the file
        os.rename(old_path, new_path)
        print(f"Renamed: '{file}' -> '{new_name}'")

if __name__ == "__main__":
    reformat_and_rename()
