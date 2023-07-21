"""
Web-скрапинг рейтинга пользовательского
рейтинга отеля
"""

from selenium import webdriver
from bs4 import BeautifulSoup
import numpy as np
from selenium.webdriver.chrome.options import Options
import pandas as pd


data = pd.read_csv('data.csv')

data_for_scraping = data[['hotel_name', 'url_short']].value_counts().reset_index()
data_for_scraping = pd.DataFrame(data_for_scraping).drop(0, axis=1)

# Отключение JS и загрузки картинок
chrome_options = Options()
chrome_options.add_argument("--disable-javascript")
chrome_options.add_experimental_option("prefs", {'profile.managed_default_content_settings.images': 2})

XPATH = 'xpath'
data_for_scraping['other_rating'] = np.nan
driver = webdriver.Chrome(executable_path="C:/Chrome/chromedriver.exe", chrome_options=chrome_options)

for i in range(len(data_for_scraping)):
    url = data_for_scraping['url_short'][i]
    print(i, data_for_scraping['hotel_name'][i])
    driver.get(url)

    soup = BeautifulSoup(driver.page_source, 'lxml')
    elements = soup.find_all('h3', {'class': 'uitk-heading uitk-heading-5 uitk-spacing uitk-spacing-padding-blockend-three'})

    for elem in elements:
        if '/' in elem.text:
            other_target = float(elem.text.split('/')[0])

    print(other_target)

    data_for_scraping['other_rating'][i] = other_target


data_for_scraping.to_csv('hotels_other_target.csv', index=False)
