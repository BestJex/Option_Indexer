#爬取所有农产品的信息
import requests
import datetime
from bs4 import BeautifulSoup


def  get_page_number():
  res=requests.get('http://www.xibeiap.com/template/xibei/jghq.jsp?market_id=27&iStart=1')
  soup=BeautifulSoup(res.text,'html.parser')
  table=soup.find('table',class_='ba').find_next_sibling('table')
  spans=table.find_all('span')
  total_page_number=spans[1].text
  return int(total_page_number)
  #print(total_page_number)
def get_one_page_data(pageNumber):
    res=requests.get('http://www.xibeiap.com/template/xibei/jghq.jsp?market_id=27&iStart='+pageNumber)
    soup=BeautifulSoup(res.text,'html.parser')
    table=soup.find('table',class_='ba')   #最后几个页面没有数据，暂时没有影响

    trs=table.find_all('tr')
    for i in range(1,len(trs)):
        tds=trs[i].find_all('td')          #数据都在这
        product_name=tds[0].text.strip()
        middle_price=tds[1].text.strip()
        change=tds[2].text.strip()
        highest_price=tds[3].text.strip()
        lowest_price=tds[4].text.strip()
        trading_amount=tds[5].text.strip()
        date=tds[7].text.strip()
        print(product_name,middle_price,change,highest_price,lowest_price,trading_amount,date)
    #print('This is page'+pageNumber)
def get_all_pages_data():
    for i in range(1,get_page_number()+1):
        page_number=str(i)
        get_one_page_data(page_number)

def daily_update():
    today= datetime.date.today()
    newest_date=today+datetime.timedelta(days=-1) #能获取到的最新的数据为当前日期的前一天
    newest_date=str(newest_date)
    for i in range(1,100): #暂时设定99，每天最多更新的页数应该不会超过19
        res = requests.get('http://www.xibeiap.com/template/xibei/jghq.jsp?market_id=27&iStart=' + str(i))
        soup = BeautifulSoup(res.text, 'html.parser')
        table = soup.find('table', class_='ba')
        trs = table.find_all('tr')
        continue_page=True
        if continue_page:
            for i in range(1, len(trs)):
                tds = trs[i].find_all('td')
                date = tds[7].text.strip()
                if date == newest_date:
                    product_name = tds[0].text.strip()  # 最新的数据在这
                    middle_price = tds[1].text.strip()
                    change = tds[2].text.strip()
                    highest_price = tds[3].text.strip()
                    lowest_price = tds[4].text.strip()
                    trading_amount = tds[5].text.strip()
                    print(product_name, middle_price, change, highest_price, lowest_price, trading_amount, date)
                else:
                    continue_page=False
                    break

if __name__=="__main__":
    get_all_pages_data()

