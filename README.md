# Automation Script (File System)

## Project Overview
Automation Script (File System) is a Python-based system that automatically monitors a folder and performs file operations without manual effort.
The project demonstrates how real-world automation tasks are handled using Python in a reliable and structured way.

---

## What does this project do?
- Continuously monitors an input folder
- Detects when a new file is created
- Performs:
  - File validation 
  - File processing (example: counting lines)
- Automatically moves files to:
     - Processed folder (on success)    
     - Error folder (on failure)
- Logs:
   - File detection
   - Validation errors
   - Processing results
   - Successful file movement
---
##  Technologies Used
- Python 3
- watchdog (for folder monitoring)
- logging module
- os module
- shutil module
- time module
---

## 📁 Project Structure
```
AUTOMATION_SCRIPT/
│
├── error_files/
│   └── text.txt              # Files that failed validation or processing
│
├── input_folder/
│   └── test.txt              # New files to be monitored
│
├── processed_files/
│   └── test.txt              # Successfully processed files
│
├── logs/
│   └── automation.log        # Application log file
│
├── src/
│   └── Scripts/
│       ├── __init__.py       # Package initializer
│       ├── file_monitor.py   # Monitors input folder for new files
│       ├── file_mover.py     # Moves files to processed or error folders
│       ├── file_processor.py # Processes files (example: line count)
│       ├── file_validator.py # Validates file type and size
│       ├── logger_config.py  # Logging configuration
│       └── main.py           # Program entry point
│
├── config.py                 # Folder paths and project configuration
├── README.md                 # Project documentation
└── requirements.txt          # Project dependencies

```
## How to Run

Follow these steps to run the Async API Data Fetcher:

### 1. Clone the repository
```
git clone https://github.com/JaspinderKaurWalia26/PROJECT-8-Automation-Script-File-System-.git
cd PROJECT-8-Automation-Script-File-System
```
### 2. Create a virtual environment (optional)
```
python -m venv venv
```
### 3. Activate the virtual environment
- Windows:
```
venv\Scripts\activate
```
- Linux/Mac:
```
source venv/bin/activate
```
### 4. Install dependencies
```
pip install -r requirements.txt
```
### 5. Run the program
```
python -m src.Scripts.main
```
### 6. Check outputs

- Processed files: processed_files
- Logs: logs/automation.log



