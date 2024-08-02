from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

# Create a Chrome webdriver instance with ChromeDriver Manager
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.tutorialsfreak.com/")
time.sleep(2)
driver.save_screenshot("C:/Users/ASUS/OneDrive/Pictures/fullpage.png")