import productListOnShop
import sqlManager
s = productListOnShop.parserOnShop().get_product_list()
sql = sqlManager.sqlManager()
sql.insert(s)
