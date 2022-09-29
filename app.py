import staristic
import productListOnShop
import sqlManager
x = staristic.getStatistic().get_statistic_search()
sqlManager.sqlManager().push_today_statistic(x)


