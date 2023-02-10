from PIL import Image
import random

# List of image filenames
image_filenames = ['image1.jpg', 'image2.jpg', 'image3.jpg', 'image4.jpg']

# Open all images and store them in a list
images = [Image.open(f) for f in image_filenames]

# Randomly shuffle the list of images
random.shuffle(images)

# Combine all images into a single image, side-by-side
widths, heights = zip(*(i.size for i in images))
total_width = sum(widths)
max_height = max(heights)
new_image = Image.new('RGB', (total_width, max_height))
x_offset = 0
for image in images:
    new_image.paste(image, (x_offset, 0))
    x_offset += image.size[0]

# Save the combined image
new_image.save('combined_image.jpg')
