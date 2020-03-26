from selenium import webdriver
import datetime
from time import sleep
import csv

def DateRange(start, end, step=1, format="%Y-%m-%d"):
    strptime, strftime = datetime.datetime.strptime, datetime.datetime.strftime
    days = (strptime(end, format) - strptime(start, format)).days
    return [strftime(strptime(start, format) + datetime.timedelta(i), format) for i in range(0, days, step)]
# 手动输入模块
# start_date = str(input('''输入查询起始日期，日期格式为'YYYY-MM-DD'''))
# end_date = str(input('''输入查询结束日期，日期格式为'YYYY-MM-DD'''))
# date_list=(DateRange(start_date, end_date))
date_list = (DateRange("2020-09-29", "2020-10-04"))
print(date_list)

url_list_date =[]
wdriver = webdriver.Chrome()

hotel_list = {'Cordis':'langham-place-beijing-capital-airport.zh-cn','FourSeasons':'bei-jing-si-ji.zh-cn'}

def ExcelWriter(self):
    pass
datapool=[]

for hotelname in hotel_list.keys():
    for i in range(len(date_list)):
        if i+1 < len(date_list):
            checkin = date_list[i]
            checkout = date_list[i+1] #入住1晚
            url = f'https://www.booking.com/hotel/cn/' \
            f'{hotel_list[hotelname]}.html?' \
            f'checkin={checkin};checkout={checkout};'
            url_list_date.append(url)
            wdriver.get(url)
            wdriver.implicitly_wait(10)
            sleep(0.5)
            # rates =  wb.find_element_by_css_selector('[class=''bui-price-display__value prco-font16-helper'']')
            rates = wdriver.find_element_by_xpath('//*[@id="hprt-table"]/tbody/tr[1]/td[3]/div/div[2]/div[1]')
            showrate = rates.text[:-1].replace(',','')
            print(str(hotelname)+ '入住日期' + str(checkin) + '价格' + str(showrate))
            datapool.append([str(hotelname),str(checkin),str(showrate)])
        else:
            break
with open('price.csv','w') as f:
    fcsv = csv.writer(f)
    fcsv.writerow(datapool)


print(url_list_date)
wdriver.close()