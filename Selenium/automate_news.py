"""
In this file we use selenium to scrape a news web page. 
Since I us MS Edge as my browser as opposed to chrome, my imports and driver setup
will probably look different from most other people.   
"""


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys             #used in this scenario to automatically press the enter key after typing the password
from selenium.webdriver.support.ui import WebDriverWait     #this replaces time.sleep. using webdriverwait is more time efficient
from selenium.webdriver.support import expected_conditions as EC

"""
below we are setting options to make browsing easier. 
disable infobars means ignoring things such as nav bars on an html file
start maximized means that the page we are scraping gets maximized, since sometimes web content gets hidden when browser is resized
disable dev shm is related to linux
no sandbox gives our script greater privileges on pages
the experimental options we added is to help our scripts not be detected by web pages

analogy: think of the driver as a remote control for a web page, and the python script is the one pushing the controller buttons
"""
def get_driver():
  options = webdriver.EdgeOptions()
  options.add_argument("disable-infobars")
  options.add_argument("start-maximized")
  options.add_argument("disable-dev-shm-usage")
  options.add_argument("no-sandbox")
  options.add_experimental_option("excludeSwitches", ["enable-automation"])
  options.add_argument("disable-blink-features=AutomationControlled")
 
  driver = webdriver.Edge(options=options)                      #the driver is responsible for launching the browser and controlling it, and allows us to use methods like find_elements() etc.
  driver.get("https://www.foxnews.com/")      #loads the web page to prepare it for scraping
  return driver
 
def main():
  driver = get_driver()

  WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.XPATH, '//article[contains(@class, "article") and contains(@class, "story-")]'))
  )

  links = driver.find_elements(By.XPATH, value='//article[contains(@class, "article") and contains(@class, "story-")]//h3[contains(@class, "title")]/a')
  
  for i, link in enumerate(links, start=1):
    title = link.text
    info_div = link.find_element(By.XPATH, './ancestor::div[contains(@class, "info")]')
    #read_time = info_div.find_element(By.XPATH, value='.//span[contains(@class, "read-time")]').text
    print(f"\n\nNEWS STORY {i}:\nTitle: {title}\n")
          #Read Time: {read_time}")



main()