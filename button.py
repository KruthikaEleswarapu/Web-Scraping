from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

# Create a Chrome webdriver instance with ChromeDriver Manager
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.tutorialsfreak.com/")
time.sleep(2)
driver.find_element_by_xpath("""/html/body/div/div[2]/div[1]/section[1]/div/div[1]/div/div/div/div[2]/button""").click()
time.sleep(5)