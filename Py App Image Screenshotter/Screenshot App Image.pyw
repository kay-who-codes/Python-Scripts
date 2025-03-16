import os
import mss
from PIL import Image

# Define the dimensions of the screenshot
width = 1280
height = 640

# Get the screen dimensions of the primary monitor
with mss.mss() as sct:
    monitor = sct.monitors[1]  # Primary monitor (index 1)
    screen_width = monitor["width"]
    screen_height = monitor["height"]

# Calculate the center of the primary monitor
center_x = screen_width // 2
center_y = screen_height // 2

# Calculate the top-left corner of the screenshot
left = center_x - (width // 2)
top = center_y - (height // 2)

# Define the region to capture
region = {
    "left": left,
    "top": top,
    "width": width,
    "height": height,
    "monitor": 1,  # Primary monitor
}

# Capture the screenshot using mss
with mss.mss() as sct:
    screenshot = sct.grab(region)

# Convert the screenshot to a PIL image
image = Image.frombytes("RGB", screenshot.size, screenshot.rgb)

# Save the screenshot to the desktop as a .png file
desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
file_path = os.path.join(desktop_path, "App Image.png")
image.save(file_path, "PNG", quality=100)  # Save with high quality

print(f"Screenshot saved to {file_path}")