from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

url = "file:///C:/Users/slarc/Desktop/test%20scrapy/testArizona/attempt2/testing.html"

driver.get(url)

html = driver.page_source

soup = BeautifulSoup(html, 'html.parser')

table = soup.find("table")

# print(table)
rows = table.findAll('a', class_='html-external-link')
print(len(rows))
