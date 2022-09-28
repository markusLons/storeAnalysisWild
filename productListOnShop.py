import re
import time

import config
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

class parserOnShop:
    def __init__(self):
        self.url = "https://www.wildberries.ru/brands/"+config.name+"?page={}"
        chrome_options = Options()
        chrome_options.add_argument("--disable-extensions")
        self.driver = webdriver.Chrome(executable_path="/home/markuslons/PycharmProjects/storeAnalysisWild/chromedriver", options=chrome_options)
    def get_product_list(self):
        products = []
        for i in range(1, 100):
            self.driver.get(self.url.format(i))
            time.sleep(2)
            page = self.driver.page_source
            soup = BeautifulSoup(page, "lxml")
            soup = soup.find('div', class_="product-card-list")
            product_cards = soup.find_all('div', class_="product-card j-card-item j-good-for-listing-event")
            for j in product_cards:
                name = j.find('span', class_="goods-name").text
                price = ""
                try:
                    price = j.find('ins', class_="lower-price").text
                except:
                    price = j.find('span', class_="lower-price").text

                index = j["id"]
                price = int(price.replace(" ", "")[:-1])
                products.append((name,price, index[1:]))
        self.driver.close()
        self.driver.quit()
        return products


