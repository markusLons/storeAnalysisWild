import staristic
import productListOnShop
import sqlManager
x = static.getStatistic().get_statistic_search()
sqlManager.sqlManager().push_today_statistic(x)


