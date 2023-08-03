# Automated OpenAI GPT-3 Chat Bot

This Python script automates a chat session with OpenAI's GPT-3 using Selenium WebDriver. It automates the process of logging into the OpenAI Chat, initiates a chat with GPT-3, and extracts the response from the model.

## Pre-requisites

Ensure you have the following installed:

- Python 3.7 and above
- Selenium
## Getting Started

These instructions will get you a copy of the project up and running on your local machine.

1. Clone the repository.

   `git clone https://github.com/username/project.git`

2. Install the requirements.

   `pip install -r requirements.txt`

3. Run the python script.

   `python script.py`

Please replace the `USERNAME` and `PASSWORD` variables in the script with your OpenAI account's username and password.

## Functions

- `get_text_by_Xpath(query)`: This function retrieves the text of a WebElement located by the Xpath provided.

- `click_button_by_Xpath(query)`: This function clicks on a WebElement located by the Xpath provided.

- `send_keys_by_Xpath(query, keys)`: This function sends keys (simulates typing) into a WebElement located by the Xpath provided.

- `sleepy_find_element(by, query, attempt_count: int = 20, sleep_duration: int = 1)`: This function is a more patient version of the Selenium find_element() function. It keeps trying to find an element up to `attempt_count` times, waiting `sleep_duration` seconds between each attempt. It's useful when working with websites that have dynamic, JS-based loading.
