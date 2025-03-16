# YouTube Video and Audio Downloader

Easily download YouTube videos or audio with these two simple scripts. Files are saved in the same directory as the scripts.

---

## Features
- **Video Downloader**: Downloads videos in the best available quality (HD).
- **Audio Downloader**: Extracts and downloads high-quality audio (e.g., MP3).
- Accepts single or multiple YouTube URLs.
- Automatic audio extraction and merging (for videos).
- Simple input GUI using `tkinter`.

---

## Requirements

### 1. **yt-dlp**
A tool for downloading videos and audio from YouTube.
- Install: `pip install yt-dlp`
- [yt-dlp GitHub](https://github.com/yt-dlp/yt-dlp)

### 2. **FFmpeg**
Handles audio extraction and video merging.
- Download: [FFmpeg Builds](https://github.com/BtbN/FFmpeg-Builds/releases)
- Add to PATH: Ensure FFmpeg is globally accessible.
- Verify: `ffmpeg -version`

---

## Usage

1. **Setup:**
   - Install `yt-dlp` and `ffmpeg`.
   - Place the scripts in a folder.

2. **Run the Script:**
   - Video or Audio Downloader: Double-click the respective script.

3. **Enter URLs:**
   - A GUI will prompt you to enter YouTube URLs (comma-separated for multiple).

4. **Output:**
   - Downloads are saved in the script directory.

---

## Troubleshooting
- **FFmpeg not found:** Ensure it is installed and added to PATH.
- **Update yt-dlp:** `pip install --upgrade yt-dlp`
- **Invalid URLs:** Check URLs for accuracy and accessibility.
- **Permissions:** Ensure you have write permissions for the directory.

---

### Helpful Links:
- [yt-dlp Documentation](https://github.com/yt-dlp/yt-dlp)
- [FFmpeg Official Site](https://ffmpeg.org/)

---

Enjoy hassle-free downloads!

