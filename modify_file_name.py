import os

root_dir = 'path/to/root/directory'
image_extensions = ['.jpg', '.jpeg', '.png', '.gif']

for dirpath, dirnames, filenames in os.walk(root_dir):
    for filename in filenames:
        ext = os.path.splitext(filename)[1].lower()
        if ext in image_extensions:
            old_file_path = os.path.join(dirpath, filename)
            new_filename = "90_" + filename
            new_file_path = os.path.join(dirpath, new_filename)
            os.rename(old_file_path, new_file_path)
