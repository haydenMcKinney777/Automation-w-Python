"""
In this file we use selenium to scrape a news web page. 
Since I us MS Edge as my browser as opposed to chrome, my imports and driver setup will probably look different from most other people.   
"""


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys             
from selenium.webdriver.support.ui import WebDriverWait     #this replaces time.sleep  -  using webdriverwait is more time efficient
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
  driver.get("https://www.foxnews.com/")                        #loads the web page to prepare it for scraping
  return driver
 
def main():
  driver = get_driver()

  news_articles_xpath = '//article[contains(@class, "article") and contains(@class, "story-")]'

  WebDriverWait(driver, 20).until(
    EC.presence_of_all_elements_located((By.XPATH, news_articles_xpath))
  )

  links = driver.find_elements(By.XPATH, value=f'{news_articles_xpath}//h3[contains(@class, "title")]/a')    #links is now a list of WebDriverElements - in this case, these elements are each of the news stories.
  
  for i, link in enumerate(links):
    title = link.text
    read_time_element = link.find_elements(By.XPATH, value='./ancestor::div[contains(@class, "info")]//span[contains(@class, "read-time")]')                #./ancestor:: is used to traverse up the DOM so that we can move further down it into the span element which contains the estimated read time text. '//' searches not just the child element, but every element under it.
    read_time = read_time_element[0].text if read_time_element else "N/A"                                                                                   #not all news articles have an estimated read time, which is why we use 'find_elements' (plural) since this will return a list regardless of if the read time is found or not. (and because we are iterating over a single link each time, the list will only ever have 1 element in it, either [] (if reading time not found) or [x] where x is the estimated reading time in the article)
    print(f"\n\nNEWS STORY {i+1}:\nTitle: '{title}'\nEstimated Read Time: {read_time}")

main()