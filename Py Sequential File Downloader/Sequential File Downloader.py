import os
import requests

def download_png_files():
    # Directory to save the downloaded PNG files
    save_directory = r"C:\Users\Kay\Desktop\PNG Files"
    
    # Ensure the directory exists
    os.makedirs(save_directory, exist_ok=True)

    # Base URL and file numbering
    base_url = "https://playingcardsio.s3.amazonaws.com/games/joking-hazard/"
    
    for i in range(1, 361):
        # Format the file number with leading zeros
        file_name = f"{i:03}.png"
        url = f"{base_url}{file_name}"
        save_path = os.path.join(save_directory, file_name)
        
        try:
            # Download the file
            response = requests.get(url, stream=True)
            response.raise_for_status()  # Raise an error for failed requests

            # Write the file to the specified directory
            with open(save_path, 'wb') as file:
                for chunk in response.iter_content(chunk_size=8192):
                    file.write(chunk)

            print(f"Downloaded: {file_name}")

        except requests.exceptions.RequestException as e:
            print(f"Failed to download {file_name}: {e}")

if __name__ == "__main__":
    download_png_files()
