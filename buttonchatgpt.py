from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# Create a Chrome webdriver instance with ChromeDriver Manager
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.tutorialsfreak.com/")

# Wait for the button to be clickable before clicking
try:
    button_xpath = "/html/body/div/div[2]/div[1]/section[1]/div/div[1]/div/div/div/div[2]/button"
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, button_xpath)))
    driver.find_element_by_xpath(button_xpath).click()
except Exception as e:
    print(f"Error: {e}")

# Add a sleep for demonstration purposes, consider using waits based on specific conditions
time.sleep(5)

# Close the browser window
driver.quit()
