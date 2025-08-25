# memobot-appium-python

## Overview
This project automates testing for the MemoBot Android app using Appium and Python.

## Prerequisites

- Python 3.8+
- [pip](https://pip.pypa.io/en/stable/)
- [Appium Server](https://appium.io/)
- Android device or emulator
- Git

## Setup

1. **Clone the repository**
   ```sh
   git clone https://github.com/thuhoaNgJ/memobot-appium-python.git
   cd memobot-appium-python
   ```

2. **Create and activate a virtual environment**
   ```sh
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```

4. **Start Appium Server**
   - Run Appium Desktop or start Appium in terminal:
     ```sh
     appium
     ```

5. **Configure device capabilities**
   - Edit `Autotest_appium.py` and update your device/emulator settings if needed.

## Running Tests

1. **Connect your Android device or start an emulator.**

2. **Run a test script**
   ```sh
   python share_audio.py
   ```

## Notes

- Make sure your device is connected and recognized by `adb`.
- Update login credentials in the test scripts as needed.
- For troubleshooting, check Appium logs and device logs.

## Project Structure

- `Autotest_appium.py` - Driver setup and configuration.
- `login.py`, `chat_AI.py`, `search_audio.py`,... - Modules.

## Running the Application

1. Open a terminal and navigate to the project directory.
2. Run a main script, for example:
   ```sh
   python check_chatAI.py
   ```
3. To create a new test file:
   - You can use `test_file.py` as a template for writing test functions.
   - There are two ways to create a new test file:
     - Duplicate `test_file.py` and modify as needed.
     - Create a new Python file and:
       - Import necessary modules, e.g. `import login.py`, `import Autotest_appium`.
       - Call the login function from `login.py`.
       - Continue writing your test functions