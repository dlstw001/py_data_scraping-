from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import time # Set time interval
import tldextract # Get domain
import string


# Setting
opts = webdriver.ChromeOptions()
opts.add_argument("--disable-notifications, --headless")
s = Service(r'C:\Users\davidl\Desktop\py_data_scraping\driver\chromedriver.exe')
global_link_lst = ["https://www.smartone.com/tc/home/"]
link = "https://www.smartone.com/tc/home/"
driver = webdriver.Chrome(service=s, options=opts)


domain = tldextract.extract(link).domain
for link in global_link_lst:
    driver.get(link)

    # Scroll down until the end
    time.sleep(3)
    previous_height = driver.execute_script('return document.body.scrollHeight')
    while True:
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
        time.sleep(3)
        new_height = driver.execute_script('return document.body.scrollHeight')
        if new_height == previous_height:
            break

    # Make BeautifulSoup
    content = driver.page_source
    soup = BeautifulSoup(content, 'lxml')
    content = soup.text.translate({ord(c): None for c in string.whitespace})
    with open('content.txt', "w", encoding="utf-8") as f:
        f.write(content)
