import logging

logger = logging.getLogger(__name__)

#processing file
def process_file(file_path):
    try:
        logger.info(f"Processing file: {file_path}")
        # opening file
        with open(file_path, "r") as f:
            lines = f.readlines()

        logger.info(f"Successfully processed {file_path} | Lines count: {len(lines)}")
        return True, f"Lines count: {len(lines)}"

    except Exception as e:
        logger.error(f"Error processing file {file_path}: {e}", exc_info=True)
        return False, str(e)
