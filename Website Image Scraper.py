import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from urllib.request import urlretrieve
from tkinter import Tk, simpledialog, messagebox
from datetime import datetime

# Create a Tkinter root window (hidden)
root = Tk()
root.withdraw()  # Hide the root window

# Prompt user for scraping options
options = ["Download all images from one webpage", "Download images from sequential URLs"]
choice = simpledialog.askstring("Image Scraper", f"Choose an option:\n1. {options[0]}\n2. {options[1]}")

if not choice or choice not in ['1', '2']:
    messagebox.showerror("Error", "Invalid selection. Exiting.")
    exit()

# Get the base URL from the user
base_url = simpledialog.askstring("Image Scraper", "Enter base URL (e.g., https://example.com):")
if not base_url:
    messagebox.showerror("Error", "No URL entered. Exiting.")
    exit()

# Create a directory for saving images in the same location as the script
script_dir = os.path.dirname(os.path.abspath(__file__))
current_date = datetime.now().strftime("%Y-%m-%d")
download_dir = os.path.join(script_dir, f"Scraped Images - {current_date}")
os.makedirs(download_dir, exist_ok=True)

if choice == '1':
    # Scrape all images from one webpage
    response = requests.get(base_url)
    if response.status_code != 200:
        messagebox.showerror("Error", f"Failed to fetch the webpage: {response.status_code}")
        exit()

    soup = BeautifulSoup(response.text, 'html.parser')
    images = soup.find_all('img')

    for img in images:
        src = img.get('src')
        if src:
            image_url = urljoin(base_url, src)
            image_name = os.path.basename(image_url)
            save_path = os.path.join(download_dir, image_name)

            print(f"Downloading {image_url} to {save_path}...")
            try:
                urlretrieve(image_url, save_path)
                print(f"Downloaded: {image_name}")
            except Exception as e:
                print(f"Failed to download {image_url}: {e}")

elif choice == '2':
    # Scrape images from sequential URLs
    start_number = simpledialog.askinteger("Image Scraper", "Enter the starting number for sequential URLs:")
    end_number = simpledialog.askinteger("Image Scraper", "Enter the ending number for sequential URLs:")

    if start_number is None or end_number is None or start_number > end_number:
        messagebox.showerror("Error", "Invalid range. Exiting.")
        exit()

    for i in range(start_number, end_number + 1):
        image_url = f"{base_url.rstrip('/')}/{i}.png"  # Adjust this format as needed
        image_name = os.path.basename(image_url)
        save_path = os.path.join(download_dir, image_name)

        print(f"Downloading {image_url} to {save_path}...")
        try:
            urlretrieve(image_url, save_path)
            print(f"Downloaded: {image_name}")
        except Exception as e:
            print(f"Failed to download {image_url}: {e}")

messagebox.showinfo("Image Scraper", "Image download process completed.")
