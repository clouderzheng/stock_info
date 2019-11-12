import requests
import json
import pandas as pd




headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) ' \
                         'Chrome/51.0.2704.63 Safari/537.36'}
session = requests.session()
session.get("https://xueqiu.com", headers=headers)
# 获取所有股票
html_data = session.get("https://xueqiu.com/service/v5/stock/screener/quote/list?page=1&size=4000&order=desc&orderby=percent&order_by=percent&market=CN&type=sh_sz&_=1573555499517", headers=headers)
loads = json.loads(html_data.text)
stock_list = loads["data"]["list"]
stock_array = []
for sotck in stock_list:
    stock_array.append(sotck["symbol"])
url = "https://stock.xueqiu.com/v5/stock/finance/cn/indicator.json?symbol={}&type=all&is_detail=true&count=23&timestamp=1573543464962"
for stock in stock_array:
    html_data = session.get(url.format(stock), headers=headers)
    json_data = json.loads(html_data.text);
    quarterly_report_list = json_data["data"]["list"]
    data = pd.DataFrame([{"quote_name":json_data["data"]["quote_name"]}])
    data.to_csv("o://sotck_info.csv", index=False, mode='a', )
    data = pd.DataFrame(quarterly_report_list)
    data.to_csv("o://sotck_info.csv",index=False,mode='a',)

