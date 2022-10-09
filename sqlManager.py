import pymysql
import config
class sqlManager:
    def __init__(self):
        host = config.sql.host
        user = config.sql.user
        password = config.sql.password
        database = config.sql.database
        port = config.sql.port
        self.db = pymysql.connect(host=host, user=user, password=password, database=database, port=port, charset='utf8mb4')
        self.cursor = self.db.cursor()
    def insert(self, products):
        for i in products:
            sql = "INSERT INTO product_on_shop (name, price, vendorCode) VALUES ('{}', '{}', {})".format(str(i[0]), i[1], i[2]).replace("''", "'")
            self.cursor.execute(sql)
        self.db.commit()
        print("insert successful!!")
    def get_keywords(self):
        print("get keywords")
        sql = "SELECT word, id FROM keywords"
        self.cursor.execute(sql)
        keywords = self.cursor.fetchall()
        return keywords
    def get_index(self):
        sql = "SELECT vendorCode FROM product_on_shop"
        self.cursor.execute(sql)
        index = self.cursor.fetchall()
        return index
    def push_today_statistic(self, statistic):
        for i in statistic:
            sql = "INSERT INTO statistic_keywordsday_to_day (dayGet, vendorCode, id_keywords, top) VALUES (NOW(), '{}', '{}', '{}');".format(str(i[0]), i[1], i[2])
            self.cursor.execute(sql)
        self.db.commit()
        print("insert successful!!")
    def get_statistic_day_to_day(self):
        sql = """select statistic_keywordsday_to_day.dayGet, statistic_keywordsday_to_day.top,
       k.word, statistic_keywordsday_to_day.vendorCode,
       statistic_keywordsday_to_day.id_keywords
from statistic_keywordsday_to_day
join product_on_shop pos on statistic_keywordsday_to_day.vendorCode = pos.vendorCode
join keywords k on statistic_keywordsday_to_day.id_keywords = k.id;"""
        self.cursor.execute(sql)
        statistic = self.cursor.fetchall()
        return statistic
    def get_info_about_today(self):
        sql = "select * from statistic_keywordsday_to_day where date(NOW()) = dayGet;"
        self.cursor.execute(sql)
        statistic = self.cursor.fetchall()
        return statistic