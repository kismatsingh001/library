# Simple Language Doc Opener

## 📖 Description

This is a simple, menu-driven Python script that runs in your terminal. It welcomes the user and provides two menus:

1.  A main menu to either continue or exit the program.
2.  A language menu that allows the user to select a topic (Python, C, Java, CSS, or HTML).

Based on the user's selection, the script uses the `webbrowser` module to automatically open the official Mozilla Developer Network (MDN) documentation page for that topic in their default web browser.

## ✨ Features

* A simple console interface.
* Provides quick access to 5 different MDN documentation pages.
* Uses the built-in `webbrowser` library to launch your system's default browser.

## 📋 Requirements

* **Python 3:** The script is written for Python 3.
* **A Web Browser:** You must have a default web browser (like Chrome, Firefox, Safari, or Edge) installed on your operating system.

## 🚀 How to Run

1.  **Save the Code:**
    Make sure the code is saved in a file named `new3.py`.

2.  **Open Your Terminal (or Command Prompt):**
    Navigate to the directory (folder) where you saved the `new3.py` file.

3.  **Run the Script:**
    Type the following command and press Enter:
    ```bash
    python new3.py
    ```

4.  **Follow the Prompts:**
    * The script will first ask you to "Press 1 to continue." or "Press 2 to exit."
    * If you choose 1, it will display the list of languages.
    * Enter the number (1-5) for the topic you want to see, and a new browser tab or window will open to that page.
    * The script will then ask if you want to run it again.
```eof
