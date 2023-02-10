from PIL import Image
import random

def make_collage(images, width, height):
    collage = Image.new("RGB", (width, height), (255, 255, 255))
    images = random.sample(images, 9)

    x_offset = 0
    y_offset = 0
    for img in images:
        collage.paste(img, (x_offset, y_offset))
        x_offset += img.width
        if x_offset >= collage.width:
            x_offset = 0
            y_offset += img.height
    return collage

if __name__ == "__main__":
    # Load the images you want to use in the collage
    images = [Image.open(f"image{i}.jpg") for i in range(1, 10)]
    # Specify the size of the final collage
    width = 3 * images[0].width
    height = 3 * images[0].height

    collage = make_collage(images, width, height)
    collage.show()
    collage.save("collage.jpg")
