from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.keys import Keys

# Create a Chrome webdriver instance with ChromeDriver Manager
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.google.com/")

search=driver.find_element_by_xpath("""/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/div/textarea""")
search.send_keys("wscubetech")
search.send_keys(Keys.ENTER)
time.sleep(5)