import logging
import os

# setting configuration of logger
def setup_logger():
    os.makedirs("logs", exist_ok=True)
     
    logger = logging.getLogger("AutomationLogger")
    logger.setLevel(logging.INFO)
    # formatter
    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"
    )
    # file handler
    file_handler = logging.FileHandler("logs/automation.log")
    file_handler.setFormatter(formatter)
    # console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    if not logger.handlers:
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger
