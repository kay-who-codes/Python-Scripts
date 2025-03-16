import pandas as pd
import os
import json

# Get the directory where the .py script is located
script_dir = os.path.dirname(os.path.realpath(__file__))

# Load the CSV file
df = pd.read_csv("A:\Programming\Kays Apps\Tools & Utilities\- Py Scripts\Py Excel to JSON\All RSS Feeds-Grid view.csv")

# Define the full path for the JSON file in the same directory as the script
json_path = os.path.join(script_dir, "NEW_JAYSON_FROM_SPREADSHEET.json")

# Convert to JSON string with escaping
json_string = df.to_json(orient="records", indent=4)

# Post-process to remove unwanted escaped slashes
json_string = json_string.replace(r'\/', '/')

# Write the cleaned JSON string to a file
with open(json_path, 'w', encoding='utf-8') as json_file:
    json_file.write(json_string)