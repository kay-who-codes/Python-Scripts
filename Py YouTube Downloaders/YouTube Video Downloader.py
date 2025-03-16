import tkinter as tk
from tkinter import simpledialog
import yt_dlp
import os

# Function to download videos using yt-dlp
def download_video(url):
    try:
        # Get the directory of the current script file (absolute path)
        script_dir = os.path.dirname(os.path.realpath(__file__))

        # Download options for yt-dlp
        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',  # Download the best quality video + audio streams
            'outtmpl': os.path.join(script_dir, '%(title)s.%(ext)s'),  # Save video in the same directory as the script
            'merge_output_format': 'mp4',  # Merge audio and video into an mp4 file
            'noplaylist': True,  # Avoid downloading playlists (in case the URL is a playlist)
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])  # Download the video
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
            download_video(url.strip())  # Download each video

if __name__ == "__main__":
    prompt_user_for_urls()
