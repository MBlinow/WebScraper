import requests, bs4
from bs4 import BeautifulSoup



##Creating cookie to bypass age gate
cookies = {'birthtime': '568022401', 'mature_content': '1'}

def printGameInfo(gameIDNum):
    requestString='http://store.steampowered.com/app/'+str(gameIDNum)+'/'
    #res = requests.get('http://store.steampowered.com/app/608800/', cookies=cookies)
    #Getting target page html
    res = requests.get(requestString, cookies=cookies)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'html.parser')
    gamePrice=soup.find(class_="price")
    if gamePrice==None:
        gamePrice=soup.find(class_="discount_final_price").string
        gamePrice=gamePrice+' on sale'
    else: gamePrice=gamePrice.string
    gameName=soup.find(class_="apphub_AppName").string
    print (gameName.encode('utf8'))
    #print (gameName)
    print (str(gamePrice).strip())

def formatUserInput(userInput):
    formattedInput=''
    for i in range(len(userInput)):
        if userInput[i]==' ':
            formattedInput+='+'
        else:
            formattedInput+=userInput[i]
    return formattedInput

def gameSearch():
    #userInput=input('Enter Game Name: ')
    userInput='Quake 2'
    formattedInput=formatUserInput(userInput)


    requestString='http://store.steampowered.com/search/?snr=1_4_4__12&term='+formattedInput
    res = requests.get(requestString)
    soup = BeautifulSoup(res.text, 'html.parser')

#printGameInfo(608800)
#printGameInfo(374320)
#printGameInfo(403640)
gameSearch()
