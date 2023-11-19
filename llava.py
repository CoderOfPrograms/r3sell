from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

# Navigate to the website
driver.get("https://llava-vl.github.io/")
element = driver.find_element(By.CSS_SELECTOR,'gradio-app')

driver.execute_script("arguments[0].scrollIntoView();", element)

# Wait for the page to load (adjust the time as needed)
time.sleep(2)

# Uploading an image

def get_quality(image_path):

    # Replace '/path/to/your/image.jpg' with the path to your image
    file_input = driver.find_element(By.CSS_SELECTOR, 'input[type="file"]')
    file_input.send_keys(image_path)

    # Wait for the upload to complete (adjust time as needed)
    time.sleep(5)

    # Locate the textarea element
    textarea = driver.find_element(By.CSS_SELECTOR, 'textarea.svelte-4xt1ch')

    # Type your message
    message = "I am planning to resell this product. Please identify any defects or issues or seems worn out or any scratches. Also, what is the color of product. Start your response with the word ANS"
    textarea.send_keys(message)

    textarea.send_keys(Keys.ENTER)

    # Wait for the action to complete (adjust time as needed)
    time.sleep(30)

    # Close the browser (optional)
    element = driver.find_elements(By.XPATH, "//*[contains(text(), 'ANS')]")[1]


    ans = element.text


    return ans