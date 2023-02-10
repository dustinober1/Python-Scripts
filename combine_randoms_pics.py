from PIL import Image
import os
import random

def create_image_grid(folder_path, grid_size, output_path):
    # Get all image files in the folder
    image_files = [f for f in os.listdir(folder_path) if f.endswith('.jpg') or f.endswith('.png')]
    # Randomly select 9 images
    selected_files = random.sample(image_files, grid_size * grid_size)
    # Open each selected image
    images = [Image.open(os.path.join(folder_path, f)) for f in selected_files]
    # Resize all images to 256x256
    images = [i.resize((256, 256)) for i in images]
    # Create a 3x3 grid of the images
    width = 256 * grid_size
    height = 256 * grid_size
    grid_image = Image.new('RGB', (width, height))
    for i, image in enumerate(images):
        x = i % grid_size * 256
        y = i // grid_size * 256
        grid_image.paste(image, (x, y))
    # Save the grid image
    grid_image.save(output_path)

create_image_grid('path/to/folder', 3, 'output.jpg')
