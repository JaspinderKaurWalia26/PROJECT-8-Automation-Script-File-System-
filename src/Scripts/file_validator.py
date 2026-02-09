import os
from config import VALID_EXTENSIONS


# validation file
def validate_file(file_path):
    # check whether its a file 
    if not os.path.isfile(file_path):
        # if its not file 
        return False, "Not a file"
    # splitting file path
    _, ext = os.path.splitext(file_path)
    # checking extension
    if ext.lower() not in VALID_EXTENSIONS:
        return False, "Invalid file type"
    # checking the file
    if os.path.getsize(file_path) == 0:
        return False, "File is empty"
    return True, "File is valid"
