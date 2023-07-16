import os

directory = '/Users/dustinober/Desktop'

for filename in os.listdir(directory):
    if filename.startswith('Screenshot'):
        file_path = os.path.join(directory, filename)
        os.remove(file_path)
        print(f"Deleted file: {filename}")
