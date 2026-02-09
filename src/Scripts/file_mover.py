import shutil
import os

# move file function
def move_file(file_path, destination):
    os.makedirs(destination, exist_ok=True)
    # moving file from input folder to processed folder
    shutil.move(file_path, os.path.join(destination, os.path.basename(file_path)))
