import os
import pandas as pd

def generate_html_table(file_name, df):
    """Generates an HTML string from the DataFrame with optimised formatting."""
    html = []
    html.append(f"<h3>{os.path.splitext(file_name)[0]}</h3>")
    html.append("<table>")

    # Create table headers
    html.append("    <thead>")
    html.append("        <tr>")
    for col in df.columns:
        html.append(f"            <th>{col}</th>")
    html.append("        </tr>")
    html.append("    </thead>")

    # Create table body
    html.append("    <tbody>")
    for _, row in df.iterrows():
        html.append("        <tr>")
        for value in row:
            html.append(f"            <td>{value if pd.notna(value) else ''}</td>")
        html.append("        </tr>")
    html.append("    </tbody>")

    html.append("</table>")
    return "\n".join(html)

def main():
    folder_path = os.path.dirname(os.path.abspath(__file__))
    output_file = os.path.join(folder_path, "NEW_HTML_TABLE.txt")

    # List to store HTML segments
    html_content = []

    # Process each CSV and Excel file in the folder
    for file in os.listdir(folder_path):
        if file.endswith(".csv"):
            df = pd.read_csv(os.path.join(folder_path, file))
            html_content.append(generate_html_table(file, df))
        elif file.endswith(".xlsx"):
            excel_file = pd.ExcelFile(os.path.join(folder_path, file))
            for sheet_name in excel_file.sheet_names:
                df = excel_file.parse(sheet_name)
                html_content.append(generate_html_table(sheet_name, df))

    # Append CSS Styling
    css_styling = """

- - - CSS STYLING - - -

.h2, .h3 {
    margin-top: 120px;
}

.table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 20px;
}

.table th, .table td {
    border: 1px solid #ddd;
    padding: 10px;
    text-align: left;
}

.table th {
    background-color: #f4f4f4;
}

body.dark-mode .table th {
    background-color: #555;
}

body.dark-mode .table th,
body.dark-mode .table td {
    border-color: #666;
}
"""

    html_content.append(css_styling)

    # Write HTML content to the output file
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n\n".join(html_content))

    print(f"HTML table saved to {output_file}")

if __name__ == "__main__":
    main()
