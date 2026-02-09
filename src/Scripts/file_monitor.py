import time
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from .logger_config import setup_logger
from .file_validator import validate_file
from .file_processor import process_file
from .file_mover import move_file
from config import INPUT_FOLDER, PROCESSED_FOLDER, ERROR_FOLDER

logger = setup_logger()

# Event handler class to handle file system events
class Handler(FileSystemEventHandler):
    # triggered when new file is created
    def on_created(self, event):
        if event.is_directory:
            return
        # getting the full path of file
        file_path = event.src_path
        logger.info(f"New file detected: {file_path}")
        time.sleep(5)
        # validating the file
        valid, msg = validate_file(file_path)
        if not valid:
            logger.error(msg)
            # moving invalid file to error files folder
            move_file(file_path, ERROR_FOLDER)
            return
        # processing the file
        processed, msg = process_file(file_path)
        logger.info(msg)
        if not processed:
            logger.error(msg)
            # moving file to error folder if processing fails
            move_file(file_path, ERROR_FOLDER)
            return
        # moving successfully processed file to processed folder
        move_file(file_path, PROCESSED_FOLDER)
        logger.info("File processed and moved successfully")

# function monitoring the input folder
def start_monitoring():
    os.makedirs(INPUT_FOLDER, exist_ok=True)
     #creating an observer to watch file system changes
    observer = Observer()
    observer.schedule(Handler(), INPUT_FOLDER, recursive=False)
    # monitoring start
    observer.start()

    logger.info("Started folder monitoring")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        # stoping observer gracefully on keyboard interrupt
        observer.stop()
    # waiting for observer to finish
    observer.join()
