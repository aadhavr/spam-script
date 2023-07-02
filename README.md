# Spam Script

My little sister told me that coding wasn't "cool." I wrote this script in a few minutes in front of her to show her that programming is cool (or at least I think so!). 

This code is a simple script that automates the process of spamming text from a file onto a target application. It utilizes the `time` and `pyautogui` modules to introduce delays and simulate keyboard input.

## Prerequisites

To run this code, you need to have the following:

- Python: Make sure you have Python installed on your system. You can download it from the official Python website: [https://www.python.org/downloads](https://www.python.org/downloads).
- pyautogui: This code relies on the `pyautogui` library to automate keyboard input. You can install it using the following command:

  ```
  python3 -m pip install pyautogui
  ```

## Getting Started

1. Clone the repository or download the code file containing the script.
2. Ensure that you have the `script.txt` file with the desired text to be spammed. Place it in the same directory as the script file.
3. Open the script file (`spam_script.py`) in a text editor.

## Usage

To use this script:

1. Run the script by executing the following command in the terminal or command prompt:

   ```
   python spam_script.py
   ```

2. After running the script, it will wait for 5 seconds (`time.sleep(5)`) to give you time to switch to the target application where you want to spam the text. In my case, this was a messaging platform.
3. Once the initial delay is over, the script will open and read the `script.txt` file line by line.
4. For each line in the file, the script will simulate keyboard typing using `pyautogui.typewrite()` to input the text.
5. After typing the line, it will simulate pressing the "enter" key using `pyautogui.press('enter')`.
6. The script will continue this process until it reaches the end of the file.

## Important Notes

- Make sure the target application where you want to spam the text is active and in focus before running the script.
- The script uses the `utf-8` encoding to read the `script.txt` file. Ensure that the file is encoded in UTF-8 format to avoid any reading issues.
- It's essential to use this script responsibly and ethically. Misusing it for spamming or other harmful activities can have legal consequences.

## Contributing

This code is provided as-is without any warranty. You are welcome to fork the repository and modify the code according to your needs. If you have any suggestions or improvements, feel free to open an issue or submit a pull request.

## License

This code is released under the [MIT License](LICENSE). Feel free to use, modify, and distribute it as per the terms of the license.

## Acknowledgements

- The `pyautogui` library is developed and maintained by Al Sweigart. More information about the library can be found at: [https://pyautogui.readthedocs.io](https://pyautogui.readthedocs.io)
