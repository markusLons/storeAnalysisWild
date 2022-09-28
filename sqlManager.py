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
        print("connect successful!!")
    def insert(self, products):
        for i in products:
            sql = "INSERT INTO product_on_shop (name, price, vendorCode) VALUES ('{}', '{}', {})".format(str(i[0]), i[1], i[2]).replace("''", "'")
            self.cursor.execute(sql)
        self.db.commit()
        print("insert successful!!")