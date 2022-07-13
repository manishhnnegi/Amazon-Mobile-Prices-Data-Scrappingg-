
#from amazon samsung phone scraping
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from openpyxl import Workbook


#launch the webdriver and site

driver = webdriver.Chrome(executable_path='E:\IMZ\chromedriver.exe')

url = "https://www.amazon.in/s?k={q}&crid=3C1FJ19Z5M303&sprefix={q}%2Caps%2C399&ref=nb_sb_noss_1"
qqq = "samsung+phone"
driver.get(url.format(q=qqq))
time.sleep(5)


#clicking to new page
#g = driver.find_element_by_xpath('//a[@aria-label="Go to page 2"]')
#g.click()


name = []
price = []


#TO FIND ALL NAMES OF MOBILES
d = driver.find_elements_by_xpath('//span[@class="a-size-medium a-color-base a-text-normal"]')
for i in d:
    g = i.text
    name.append(g)
    #print(g)



#TO FIND PRICE
k = driver.find_elements_by_xpath('//span[@class="a-price-whole"]')
for q in k:
    m = q.text
    price.append(m)
    #print(q.text)



final = zip(name, price)
#for j in final:
    #print(j)
type(final)

#creating excel file
wb = Workbook()
sh1 = wb.active

for x in list(final):
    sh1.append(x)
sh1
#print(sh1)
wb.save("final.xlsx")
driver.implicitly_wait(10)
print("2")





