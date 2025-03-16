import tkinter as tk
from tkinter import simpledialog
import yt_dlp
import os

# Function to download audio using yt-dlp
def download_audio(url):
    try:
        # Get the directory of the current script file (absolute path)
        script_dir = os.path.dirname(os.path.realpath(__file__))

        # Download options for yt-dlp
        ydl_opts = {
            'format': 'bestaudio/best',  # Download the best quality audio stream
            'outtmpl': os.path.join(script_dir, '%(title)s.%(ext)s'),  # Save audio in the same directory as the script
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',  # Save as mp3 (you can change to 'aac', 'm4a', etc.)
                'preferredquality': '192',  # Audio quality (192 kbps)
            }],
            'noplaylist': True,  # Avoid downloading playlists (in case the URL is a playlist)
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])  # Download the audio
            print(f"Downloaded: {url}")
    except Exception as e:
        print(f"Error downloading {url}: {str(e)}")

# Create a simple GUI using tkinter
def prompt_user_for_urls():
    # Set up the dialog box
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    # Prompt the user for YouTube URLs
    urls = simpledialog.askstring("YouTube URL Input", "Enter YouTube video URLs (separate multiple URLs with commas):")

    if urls:
        urls = urls.split(",")  # Split URLs by comma
        for url in urls:
            download_audio(url.strip())  # Download each audio

if __name__ == "__main__":
    prompt_user_for_urls()
