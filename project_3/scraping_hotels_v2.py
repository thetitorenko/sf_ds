from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import numpy as np
from time import sleep


def scraping_hotels_v2(hotel_name: str) -> list:
    """
    Web-скрапинг рейтинга отеля по его имени
    """
    print('Ищем', hotel_name)

    XPATH = 'xpath'
    url = 'https://hotels.com'
    star = np.nan

    try:
        driver = webdriver.Chrome(executable_path="C:/Chrome/chromedriver.exe")
        driver.get(url)

        driver.find_element(
            By.XPATH, "//button[@data-stid='destination_form_field-dialog-trigger']"
            ).click()

        driver.find_element(
            By.XPATH, "//input[@id='destination_form_field']"
            ).send_keys(hotel_name)
        sleep(3)

        driver.find_element(
            By.XPATH, "//button[@data-stid='destination_form_field-result-item-button']"
            ).click()

        driver.find_element(
            By.XPATH, "//button[@id='search_button']"
            ).click()

        hotel_url = driver.find_element(
            By.XPATH, "//a[@data-stid='open-hotel-information']"
        ).get_attribute('href')

        driver.get(hotel_url)

        soup = BeautifulSoup(driver.page_source, 'lxml')
        star_draft = soup.find_all('div', {'class': 'uitk-text uitk-type-300 uitk-text-default-theme'})

        for elem in star_draft:
            if 'star' in elem.text.split()[0][-4:]:
                star = float(elem.text.split()[0].split('-')[0])
                driver.close()
                break

        print('    найдена оценка', star)
        return [star, hotel_url]

    except Exception:
        driver.close()
        print('    ошибка')
        return [star, np.nan]
