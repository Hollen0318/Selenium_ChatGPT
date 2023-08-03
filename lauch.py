# selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

SLEEP_TIME = 2
USERNAME = "your username"
PASSWORD = "your password"

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# Go to a login page
driver.get("https://chat.openai.com/auth/login")
time.sleep(SLEEP_TIME)

def get_text_by_Xpath(query):
    text = sleepy_find_element(By.XPATH, query).text
    return text

def click_button_by_Xpath(query):
    button = sleepy_find_element(By.XPATH, query)
    button.click()
    time.sleep(SLEEP_TIME)

def send_keys_by_Xpath(query, keys):
    field =  sleepy_find_element(By.XPATH, query)
    field.send_keys(keys)
    time.sleep(SLEEP_TIME)

def sleepy_find_element(by, query, attempt_count: int = 20, sleep_duration: int = 1):
    """If the loading time is a concern, this function helps"""
    for _ in range(attempt_count):
        item = driver.find_elements(by, query)
        if len(item) > 0:
            item = item[0]
            break
        else:
            return "not found"
        time.sleep(sleep_duration)
    return item


# Click the login button
login_button = sleepy_find_element(By.XPATH, '//*[@id="__next"]/div[1]/div[2]/div[1]/div/button[1]')
if login_button == "not found":
    click_button_by_Xpath('//*[@id="__next"]/div[1]/div[1]/div[4]/button[1]/div')
else:
    click_button_by_Xpath('//*[@id="__next"]/div[1]/div[2]/div[1]/div/button[1]')
# Write a username using XPath
send_keys_by_Xpath('//*[@id="username"]', USERNAME)

# Click the continue using XPath
click_button_by_Xpath('/html/body/div/main/section/div/div/div/div[1]/div/form/div[2]/button')

# Write a password using XPath
send_keys_by_Xpath('//*[@id="password"]', PASSWORD)

# Click the login button using XPath
click_button_by_Xpath('/html/body/div/main/section/div/div/div/form/div[3]/button')

# Click the next next start buttons if present:
if sleepy_find_element(By.XPATH, '//*[@id="radix-:ri:"]/div[2]/div/div[2]/button/div') != "not found":
    click_button_by_Xpath('//*[@id="radix-:ri:"]/div[2]/div/div[2]/button/div')
    click_button_by_Xpath('//*[@id="radix-:ri:"]/div[2]/div/div[2]/button[2]/div')
    click_button_by_Xpath('//*[@id="radix-:ri:"]/div[2]/div/div[2]/button[2]/div')

# Click the new chat button to start a new chat
click_button_by_Xpath('//*[@id="__next"]/div[1]/div[1]/div/div/div/nav/div[1]/a')
# Send some keys to the text area
send_keys_by_Xpath('//*[@id="prompt-textarea"]', "introduce your self")
# Click the dismiss button if found
if sleepy_find_element(By.XPATH, '//*[@id="__next"]/div[2]/ol/li/button[1]/div') != "not found":
    click_button_by_Xpath('//*[@id="__next"]/div[2]/ol/li/button[1]/div')
# Click the send button
click_button_by_Xpath('//*[@id="__next"]/div[1]/div[2]/div/main/div[2]/form/div/div[2]/button')
# Extract the answers from the GPT3
text = get_text_by_Xpath('//*[@id="__next"]/div[1]/div[2]/div/main/div[1]/div/div/div/div[2]/div')
print(f"return text = \n{text}")
# Write something in a search field using XPath
driver.quit()
