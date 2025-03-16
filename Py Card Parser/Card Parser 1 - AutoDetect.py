from PIL import Image, ImageDraw, ImageOps
import os

# Function to add rounded corners to an image
def add_rounded_corners(image, radius):
    """Add rounded corners to an image.
    Args:
        image (PIL.Image.Image): The image to modify.
        radius (int): Radius of the rounded corners.

    Returns:
        PIL.Image.Image: The image with rounded corners.
    """
    # Create a mask for the rounded corners
    rounded_mask = Image.new("L", image.size, 0)
    draw = ImageDraw.Draw(rounded_mask)
    draw.rounded_rectangle(
        [(0, 0), image.size],
        radius=radius,
        fill=255
    )
    # Apply the mask to the image
    rounded_image = image.convert("RGBA")
    rounded_image.putalpha(rounded_mask)
    return rounded_image

# Function to find all supported image files in the same directory as the script
def find_image_files():
    """Search for all supported image files (JPG, JPEG, PNG) in the script's folder.

    Returns:
        list: A list of file paths to the image files.
    """
    supported_extensions = [".jpg", ".jpeg", ".png", ".pdf"]
    script_directory = os.path.dirname(os.path.abspath(__file__))
    return [
        os.path.join(script_directory, file)
        for file in os.listdir(script_directory)
        if os.path.splitext(file)[1].lower() in supported_extensions
    ]

# Main execution starts here
if __name__ == "__main__":
    # Find all image files in the script's directory
    image_files = find_image_files()

    # Create a folder named "Individual PNGs" for output
    output_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Individual PNGs")
    os.makedirs(output_folder, exist_ok=True)  # Ensure the output folder exists

    # Define grid dimensions and corner radius
    rows, cols = 7, 10  # Adjust grid dimensions as needed
    corner_radius = 20  # Adjust the corner radius for rounded corners

    print(f"Found {len(image_files)} image files. Processing...")

    # Process each image file
    for file_index, image_file in enumerate(image_files, start=1):
        try:
            # Load the image
            grid_image = Image.open(image_file)
            grid_width, grid_height = grid_image.size

            # Calculate card dimensions
            card_width = grid_width // cols
            card_height = grid_height // rows

            # Extract cards
            for row in range(rows):
                for col in range(cols):
                    left = col * card_width
                    upper = row * card_height
                    right = left + card_width
                    lower = upper + card_height

                    # Crop individual card
                    card = grid_image.crop((left, upper, right, lower))

                    # Add rounded corners to the card
                    rounded_card = add_rounded_corners(card, corner_radius)

                    # Save the card
                    card_filename = f"{os.path.splitext(os.path.basename(image_file))[0]}_r{row + 1}_c{col + 1}.png"
                    rounded_card.save(os.path.join(output_folder, card_filename))

            print(f"Processed file {file_index}/{len(image_files)}: {os.path.basename(image_file)}")
        except Exception as e:
            print(f"Error processing {os.path.basename(image_file)}: {e}")

    print(f"All images processed. Individual cards saved to '{output_folder}'.")