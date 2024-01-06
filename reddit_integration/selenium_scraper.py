from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os 
import requests
import base64
from dotenv import load_dotenv

# Function to check if image_data is too small, indicating an empty image
def is_image_empty(image_data):
    return len(image_data) < 1000  # Threshold for an empty image, may need adjustment

# Initialize the WebDriver
driver = webdriver.Chrome()  # Ensure you have the chromedriver installed

# Now you can use os.environ to get the environment variables
REDDIT_USERNAME = os.environ.get('REDDIT_USERNAME')
REDDIT_PASSWORD = os.environ.get('REDDIT_PASSWORD')


# Open Reddit login page
driver.get("https://www.reddit.com/login/")

# Wait for the login form to load
wait = WebDriverWait(driver, 10)

# Find and fill the username field
username_field = wait.until(EC.presence_of_element_located((By.ID, 'loginUsername')))
username_field.send_keys('REDDIT_USERNAME')

# Find and fill the password field
password_field = driver.find_element(By.ID, 'loginPassword')
password_field.send_keys('REDDIT_PASSWORD')

# Find and click the login button
login_button = driver.find_element(By.XPATH, '//button[contains(text(), "Log In")]')
login_button.click()

# Wait for the home page to load
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[data-testid="post-container"]')))

# Create a directory for images if it doesn't exist
image_directory = 'reddit_images'
if not os.path.exists(image_directory):
    os.makedirs(image_directory)

# Scroll down the page to ensure images are loaded
scroll_pause_time = 1
screen_height = driver.execute_script("return window.screen.height;")
images_downloaded = 0

while images_downloaded < 10:
    # Scroll down
    driver.execute_script(f"window.scrollTo(0, {screen_height * (images_downloaded // 2)});")
    time.sleep(scroll_pause_time)
    
    # Inside the loop after scrolling
    image_elements = driver.find_elements(By.CSS_SELECTOR, 'img')

    for image_element in image_elements[:10]:  # Limit to the first 10 images
        src = image_element.get_attribute('src')
        
        if src.startswith('data:image'):
            # Base64 encoded image
            base64_string = src.split('base64,')[-1]
            image_data = base64.b64decode(base64_string)
            if is_image_empty(image_data):
                continue  # Skip saving this image
            image_filename = f'reddit_images/image_{images_downloaded}.png'  # Assuming PNG format
        else:
            # Standard image URL
            response = requests.get(src)
            if response.status_code == 200:
                image_data = response.content
                if is_image_empty(image_data):
                    continue  # Skip saving this image
                image_filename = f'reddit_images/image_{images_downloaded}.jpg'  # Assuming JPG format

        # Save the image data
        with open(image_filename, 'wb') as file:
            file.write(image_data)
        images_downloaded += 1
        if images_downloaded >= 10:
            break

# Close the driver
driver.quit()




# # Initialize the WebDriver
# driver = webdriver.Chrome()  # Ensure you have the chromedriver installed

# # Open Reddit login page
# driver.get("https://www.reddit.com/login/")

# # Wait for the login form to load
# wait = WebDriverWait(driver, 10)

# # Find and fill the username field
# username_field = wait.until(EC.presence_of_element_located((By.ID, 'loginUsername')))
# username_field.send_keys('blackmamba24890')

# # Find and fill the password field
# password_field = driver.find_element(By.ID, 'loginPassword')
# password_field.send_keys('Huggies55!?')

# # Find and click the login button
# login_button = driver.find_element(By.XPATH, '//button[contains(text(), "Log In")]')
# login_button.click()

# # Wait for the home page to load
# wait.until(EC.visibility_of_element_located((By.ID, 'SHORTCUT_FOCUSABLE_DIV')))

# # Scroll down the page to ensure images are loaded
# scroll_pause_time = 1
# screen_height = driver.execute_script("return window.screen.height;")
# for i in range(5):
#     driver.execute_script(f"window.scrollTo(0, {screen_height * i});")
#     time.sleep(scroll_pause_time)

# # Add code here to find and download images

# # Close the driver
# driver.quit()
