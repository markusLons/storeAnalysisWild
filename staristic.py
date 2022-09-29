import re
import time

import config
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

import sqlManager


class getStatistic:
    def __init__(self):
        self.url = "https://www.wildberries.ru/brands/" + config.name + "?page={}"
        chrome_options = Options()
        chrome_options.add_argument("--disable-extensions")
        self.driver = webdriver.Chrome(
            executable_path="/home/markuslons/PycharmProjects/storeAnalysisWild/chromedriver", options=chrome_options)
    def get_statistic_search(self):
        url = "https://www.wildberries.ru/catalog/0/search.aspx?page={}&sort=popular&search={}"
        statistic = []
        for now_keyword in sqlManager.sqlManager().get_keywords():
            number = 0
            for i in range(1, config.statistic.max_page_for_search_statistic):
                self.driver.get(url.format(i, now_keyword[0]))
                time.sleep(config.statistic.wait_time)
                page = soup = product_cards = 0
                try:
                    page = self.driver.page_source
                    soup = BeautifulSoup(page, "lxml")
                    soup = soup.find('div', class_="product-card-list")
                    product_cards = soup.find_all('a', class_="product-card__main j-card-link")
                except Exception as e:
                    time.sleep(config.statistic.exeption_wait_time)
                    page = self.driver.page_source
                    soup = BeautifulSoup(page, "lxml")
                    soup = soup.find('div', class_="product-card-list")
                    product_cards = soup.find_all('a', class_="product-card__main j-card-link")
                for j in product_cards:
                    number+= 1
                    index = int(re.findall(r'\d+', j["href"])[0])
                    for k in [int(x[0]) for x in sqlManager.sqlManager().get_index()]:
                        if index == k:
                            statistic.append((index, now_keyword[1], number))
        return statistic




