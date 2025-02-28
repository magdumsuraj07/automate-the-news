from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import pandas as pd


chrome_options = Options()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
website = "https://www.thesun.co.uk/sport/football/"

driver.get(website)
containers = driver.find_elements(by=By.XPATH, value='//div[@class="teaser__copy-container"]')

titles = []
subtitles = []
links = []
for container in containers:
    try:
        title = container.find_element(by=By.XPATH, value='./a/span').text
        subtitle = container.find_element(by=By.XPATH, value='./a/h3').text
        link = container.find_element(by=By.XPATH, value='./a').get_attribute("href")
    except NoSuchElementException:
        print("Element does not exist. Skipping to next news.")
        continue
    titles.append(title)
    subtitles.append(subtitle)
    links.append(link)

df_headlines = pd.DataFrame({
    "title": titles,
    "subtitle": subtitles,
    "link": links
})

df_headlines.to_csv("headline-headless.csv")

driver.quit()
