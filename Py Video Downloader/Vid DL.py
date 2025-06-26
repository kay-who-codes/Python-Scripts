import os
import pytube
import yt_dlp as youtube_dl
import threading
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

class VideoDownloaderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Video Downloader")
        self.root.geometry("600x450")
        
        # Add flag for cancellation
        self.cancel_flag = False
        self.download_thread = None
        
        self.create_widgets()
    
    def create_widgets(self):
        # URL Entry
        tk.Label(self.root, text="Video URL:").pack(pady=(20, 5))
        self.url_entry = tk.Entry(self.root, width=70)
        self.url_entry.pack()
        
        # Quality Selection
        tk.Label(self.root, text="Select Quality:").pack(pady=(10, 5))
        self.quality_var = tk.StringVar(value="highest")
        qualities = ["Highest", "720p", "480p", "360p", "Lowest"]
        self.quality_menu = ttk.Combobox(self.root, textvariable=self.quality_var, values=qualities, state="readonly")
        self.quality_menu.pack()
        
        # Format Selection
        tk.Label(self.root, text="Select Format:").pack(pady=(10, 5))
        self.format_var = tk.StringVar(value="mp4")
        formats = ["mp4", "webm", "mp3 (audio only)"]
        self.format_menu = ttk.Combobox(self.root, textvariable=self.quality_var, values=formats, state="readonly")
        self.format_menu.pack()
        
        # Download Location
        tk.Label(self.root, text="Download Location:").pack(pady=(10, 5))
        self.location_var = tk.StringVar(value="A:\\Videos")
        location_frame = tk.Frame(self.root)
        location_frame.pack()
        self.location_entry = tk.Entry(location_frame, width=50, textvariable=self.location_var)
        self.location_entry.pack(side=tk.LEFT, padx=(0, 5))
        tk.Button(location_frame, text="Browse", command=self.browse_location).pack(side=tk.LEFT)
        
        # Button Frame
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=20)
        
        # Download Button
        self.download_button = tk.Button(
            button_frame, 
            text="Download Video", 
            command=self.start_download_thread,
            bg="#4CAF50", 
            fg="white"
        )
        self.download_button.pack(side=tk.LEFT, padx=10)
        
        # Cancel Button (initially disabled)
        self.cancel_button = tk.Button(
            button_frame,
            text="Cancel Download",
            command=self.cancel_download,
            bg="#f44336",
            fg="white",
            state=tk.DISABLED
        )
        self.cancel_button.pack(side=tk.LEFT, padx=10)
        
        # Progress Bar
        self.progress = ttk.Progressbar(self.root, orient=tk.HORIZONTAL, length=400, mode='determinate')
        self.progress.pack(pady=10)
        
        # Status Label
        self.status_label = tk.Label(self.root, text="", fg="blue")
        self.status_label.pack()
    
    def browse_location(self):
        folder = filedialog.askdirectory(initialdir=self.location_var.get())
        if folder:
            self.location_var.set(folder)
    
    def start_download_thread(self):
        """Start the download in a separate thread to keep the UI responsive"""
        self.cancel_flag = False
        self.download_thread = threading.Thread(target=self.download_video)
        self.download_thread.start()
        
        # Update UI
        self.download_button.config(state=tk.DISABLED)
        self.cancel_button.config(state=tk.NORMAL)
    
    def cancel_download(self):
        """Set the cancel flag and update UI"""
        self.cancel_flag = True
        self.status_label.config(text="Cancelling download...", fg="orange")
        self.cancel_button.config(state=tk.DISABLED)
    
    def update_progress(self, stream, chunk, bytes_remaining):
        if self.cancel_flag:
            raise Exception("Download cancelled by user")
            
        total_size = stream.filesize
        bytes_downloaded = total_size - bytes_remaining
        percentage = (bytes_downloaded / total_size) * 100
        self.progress['value'] = percentage
        self.status_label.config(text=f"Downloading: {percentage:.1f}%")
        self.root.update_idletasks()
    
    def download_video(self):
        url = self.url_entry.get().strip()
        if not url:
            messagebox.showerror("Error", "Please enter a valid URL")
            return
        
        download_location = self.location_var.get()
        if not os.path.isdir(download_location):
            messagebox.showerror("Error", "Invalid download location")
            return
        
        quality = self.quality_var.get().lower()
        format_type = self.format_var.get().lower()
        
        try:
            self.status_label.config(text="Starting download...", fg="blue")
            self.root.update_idletasks()
            
            # Check if YouTube
            if "youtube.com" in url or "youtu.be" in url:
                self.download_youtube_video(url, download_location, quality, format_type)
            else:
                self.download_with_ytdlp(url, download_location, quality, format_type)
            
            if not self.cancel_flag:
                self.status_label.config(text="Download completed successfully!", fg="green")
                messagebox.showinfo("Success", "Video downloaded successfully!")
                self.progress['value'] = 0
        except Exception as e:
            if str(e) != "Download cancelled by user":
                self.status_label.config(text=f"Error: {str(e)}", fg="red")
                messagebox.showerror("Error", f"Failed to download video: {str(e)}")
            else:
                self.status_label.config(text="Download cancelled", fg="orange")
            self.progress['value'] = 0
        finally:
            # Reset UI
            self.download_button.config(state=tk.NORMAL)
            self.cancel_button.config(state=tk.DISABLED)
            self.cancel_flag = False
    
    def download_youtube_video(self, url, location, quality, format_type):
        yt = pytube.YouTube(url, on_progress_callback=self.update_progress)
        
        if format_type == "mp3 (audio only)":
            stream = yt.streams.get_audio_only()
        else:
            if quality == "highest":
                stream = yt.streams.get_highest_resolution()
            elif quality == "lowest":
                stream = yt.streams.get_lowest_resolution()
            else:
                stream = yt.streams.filter(res=quality, file_extension='mp4').first()
                if not stream:
                    stream = yt.streams.get_highest_resolution()
        
        self.status_label.config(text=f"Downloading: {yt.title}", fg="blue")
        out_file = stream.download(output_path=location)
        
        # Check for cancellation before final processing
        if self.cancel_flag:
            if os.path.exists(out_file):
                os.remove(out_file)
            raise Exception("Download cancelled by user")
        
        # Rename if audio only
        if format_type == "mp3 (audio only)":
            base, ext = os.path.splitext(out_file)
            new_file = base + '.mp3'
            os.rename(out_file, new_file)
    
    def download_with_ytdlp(self, url, location, quality, format_type):
        ydl_opts = {
            'progress_hooks': [self.ytdlp_progress_hook],
            'outtmpl': os.path.join(location, '%(title)s.%(ext)s'),
            'noplaylist': True,
        }
        
        if format_type == "mp3 (audio only)":
            ydl_opts.update({
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
            })
        else:
            if quality == "highest":
                ydl_opts['format'] = 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best'
            elif quality == "lowest":
                ydl_opts['format'] = 'worstvideo[ext=mp4]+worstaudio[ext=m4a]/worst[ext=mp4]/worst'
            else:
                ydl_opts['format'] = f'bestvideo[height<={quality[:-1]}][ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best'
        
        try:
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                info_dict = ydl.extract_info(url, download=False)
                self.status_label.config(text=f"Downloading: {info_dict.get('title', 'video')}", fg="blue")
                self.root.update_idletasks()
                
                # Start download in a way that can be cancelled
                def download():
                    ydl.download([url])
                
                download_thread = threading.Thread(target=download)
                download_thread.start()
                
                while download_thread.is_alive():
                    if self.cancel_flag:
                        # This will raise an exception in the download thread
                        ydl._ies[0]._cancel_download()
                        download_thread.join()
                        raise Exception("Download cancelled by user")
                    self.root.update()
                    download_thread.join(0.1)
                
        except Exception as e:
            if str(e) != "Download cancelled by user":
                raise
            else:
                # Clean up partially downloaded file
                filename = ydl.prepare_filename(info_dict)
                if os.path.exists(filename):
                    os.remove(filename)
                raise
    
    def ytdlp_progress_hook(self, d):
        if self.cancel_flag:
            raise youtube_dl.DownloadError("Download cancelled by user")
            
        if d['status'] == 'downloading':
            total_bytes = d.get('total_bytes') or d.get('total_bytes_estimate')
            if total_bytes:
                downloaded_bytes = d['downloaded_bytes']
                percentage = (downloaded_bytes / total_bytes) * 100
                self.progress['value'] = percentage
                self.status_label.config(text=f"Downloading: {percentage:.1f}%", fg="blue")
                self.root.update_idletasks()

def main():
    root = tk.Tk()
    app = VideoDownloaderApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()