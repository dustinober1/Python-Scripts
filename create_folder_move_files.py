import os
import shutil

# Create folders for characters A-Z and 0-9
for i in [chr(x) for x in range(65, 91)] + [str(x) for x in range(10)]:
    os.mkdir(i)

# Loop through every .png file
for file in [f for f in os.listdir() if f.endswith('.png')]:
    # Get the first character of the file name
    first_char = file[0]
    
    # Move the file to the corresponding folder
    shutil.move(file, first_char)
