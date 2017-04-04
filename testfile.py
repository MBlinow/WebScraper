import requests, bs4
from bs4 import BeautifulSoup

cookies = {'birthtime': '568022401'}
res = requests.get('http://store.steampowered.com/app/431240/', cookies=cookies)
res.raise_for_status()

soup = BeautifulSoup(res.text, 'html.parser')


#print (soup.find(class_="game_area_purchase_game"))
price=soup.select('.discount_final_price')
print (soup.find(class_="discount_final_price").contents)
#print (price)


#print (soup.prettify)

