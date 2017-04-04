import requests, bs4
from bs4 import BeautifulSoup



##Creating cookie to bypass age gate
cookies = {'birthtime': '568022401', 'mature_content': '1'}

#Getting target page html
res = requests.get('http://store.steampowered.com/app/608800/', cookies=cookies)
res.raise_for_status()

soup = BeautifulSoup(res.text, 'html.parser')


gamePrice=soup.find(class_="price").string
gameName=soup.find(class_="apphub_AppName").string



print (str(gamePrice).strip())
