# Online Class Attender

## Introduction

This project aims to automate the process of joining Gmeet classes and sending a good morning message in the chat box, making attending online classes a hands-free experience. The script uses the Selenium package in Python to interact with the Gmeet website.

## Requirements

To run this program, you need to install the Chrome WebDriver and have the following Python packages:

- `selenium`
- `time`
- `datetime`

## How It Works

The script fetches the class name from the source code files, presses buttons using the Action method in Selenium, and opens the Gmeet website using WebDriver. It leverages WebDriver's ability to interact with web elements, like clicking buttons, to join the classes automatically.

## Usage

1. Install the required Python packages using `pip`:
   ```
   pip install selenium
   ```

2. Download and install the Chrome WebDriver. Ensure it is in your system's PATH.

3. Clone this repository and navigate to the project directory.

4. Run the Python script:
   ```
   python gmeet_attender.py
   ```

5. Enjoy hands-free attendance in your Gmeet classes!

**Note:** Google may block automated requests to Gmeet, rendering the automation ineffective.

## Disclaimer

This project was developed for educational purposes and to showcase automation capabilities using Selenium. Please use it responsibly and respect the policies and terms of service of the platforms you interact with.

## Contributions

Contributions and improvements to this project are welcome. Feel free to open issues and pull requests.

## License

This project is licensed under the [MIT License](LICENSE).
