import os
from PIL import Image, ImageDraw, ImageFont

# Define the text to be written
text = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

# Get a list of all the font files in the system fonts directory
font_directory = "/Users/Shared/fonts"
font_files = [os.path.join(font_directory, font_file) for font_file in os.listdir(font_directory) if font_file.endswith(".ttf")]

# Loop through each font file
for font_file in font_files:
    # Open the font file
    font = ImageFont.truetype(font_file, 48)

    # Loop through each letter in the text
    for char in text:
        # Create a blank image
        img = Image.new("RGB", (100, 100), (255, 255, 255))

        # Create a draw object to draw on the image
        draw = ImageDraw.Draw(img)

        # Draw the text on the image
        draw.text((20, 20), char, font=font, fill=(0, 0, 0))

        # Get the name of the font file without the path or extension
        font_name = os.path.splitext(os.path.basename(font_file))[0]

        # Save the image with the name of the font style and letter
        filename = f"{char}_{font_name}.png"
        img.save(filename)
