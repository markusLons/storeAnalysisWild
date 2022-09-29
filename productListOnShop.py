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
        for i in range(1, 10):
            self.driver.get(self.url.format(i))
            time.sleep(3)
            page = self.driver.page_source
            soup = BeautifulSoup(page, "lxml")
            soup = soup.find('div', class_="product-card-list")
            product_cards = soup.find_all('a', class_="product-card__main j-card-link")
            for j in product_cards:
                name = j.find('span', class_="goods-name").text
                price = ""
                try:
                    price = j.find('ins', class_="lower-price").text
                except:
                    price = j.find('span', class_="lower-price").text
                index = re.findall(r'\d+', j["href"])[0]
                price = "".join(re.findall(r'\d+', price))
                products.append((name,price, index))
        self.driver.close()
        self.driver.quit()
        return products


