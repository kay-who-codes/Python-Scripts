from PIL import Image, ImageDraw, ImageOps
import os

# Function to add rounded corners
def add_rounded_corners(image, radius):
    """Add rounded corners to an image."""
    # Create a mask for the rounded corners
    rounded_mask = Image.new("L", image.size, 0)
    draw = ImageDraw.Draw(rounded_mask)
    draw.rounded_rectangle(
        [(0, 0), image.size],
        radius=radius,
        fill=255
    )
    # Apply the mask to the image
    rounded_image = ImageOps.fit(image, image.size, centering=(0.5, 0.5))
    rounded_image.putalpha(rounded_mask)
    return rounded_image

# File paths
source_files = [
    r"FILE_LOCATION_GOES_HERE",
    r"FILE_LOCATION_GOES_HERE"
]output_folder

output_folder = r"OUTPUT_LOCATION"
os.makedirs(output_folder, exist_ok=True)  # Ensure the output directory exists

# Grid dimensions
rows, cols = 7, 10  # 7 rows and 10 columns
corner_radius = 20  # Radius for rounded corners (adjust as needed)

# Process each source file
for file_index, source_file in enumerate(source_files, start=1):
    # Load the image
    grid_image = Image.open(source_file)
    grid_width, grid_height = grid_image.size

    # Calculate card dimensions
    card_width = grid_width // cols
    card_height = grid_height // rows

    # Extract cards
    cards = []
    for row in range(rows):
        for col in range(cols):
            left = col * card_width
            upper = row * card_height
            right = left + card_width
            lower = upper + card_height

            # Crop individual card
            card = grid_image.crop((left, upper, right, lower))
            cards.append(card)

    # Save individual cards with rounded corners
    back_card = cards[-1]  # The last card in the grid is the back card
    for i, card in enumerate(cards[:-1], start=1):  # Exclude the last card from main cards
        rounded_card = add_rounded_corners(card, corner_radius)
        rounded_card.save(os.path.join(output_folder, f"grid{file_index}_card_{i}.png"))
    
    # Save the back card with rounded corners
    rounded_back = add_rounded_corners(back_card, corner_radius)
    rounded_back.save(os.path.join(output_folder, f"grid{file_index}_back.png"))

print(f"Processed {len(source_files)} files and saved cards to {output_folder}")
