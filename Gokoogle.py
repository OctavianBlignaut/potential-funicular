from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up the WebDriver
driver = webdriver.Chrome()  # Replace with your browser's WebDriver (e.g., Firefox, Edge)

try:
    # Navigate to Google
    driver.get("https://www.google.com/")
    driver.maximize_window()

    # Accept cookies if prompted (optional, depends on location)
    try:
        accept_cookies = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='I agree']"))
        )
        accept_cookies.click()
    except Exception:
        pass  # Ignore if the cookies prompt doesn't appear

    # Locate the search bar and search for "Goku and Gohan anime pictures"
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "q"))
    )
    search_box.send_keys("www.primape.net")
    search_box.send_keys(Keys.RETURN)



 # Wait for the search results to load and locate the first result
    first_result = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//h3"))
    )
    print("First result title:", first_result.text)

    # Click on the first result
    first_result.click()

    # Optional: Wait to ensure the page loads
    time.sleep(2)
except Exception:
    pass  # Ignore if the cookies prompt doesn't appear

try:
    # Navigate to the home page
    driver.get("https://primape.net")  # Replace with the actual URL
    driver.maximize_window()

    # Wait for the menu element to load
    menu = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//nav[contains(@class, 'menu')]"))
    )


    # Locate and click on a specific menu item (e.g., "About Us")
    menu_item = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Menu')]"))
    )
    menu_item.click()

    # Wait to ensure the page has navigated
    time.sleep(5)

    print("Successfully navigated the menu and clicked an item.")
finally:
    # Close the browser after a short delay
    driver.quit()











