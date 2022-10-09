import time

import staristic
import productListOnShop
import sqlManager
#x = staristic.getStatistic().get_search_data_statistic()
#staristic.getStatistic().create_statistic()
#sqlManager.sqlManager().push_today_statistic(x)
while True:
    if(sqlManager.sqlManager().get_info_about_today() == ()):
        print("no data")
        x = staristic.getStatistic().get_search_data_statistic()
        sqlManager.sqlManager().push_today_statistic(x)
    else:
        time.sleep(60*60)


