import requests, bs4
from bs4 import BeautifulSoup



##Creating cookie to bypass age gate
cookies = {'birthtime': '568022401', 'mature_content': '1'}

def printGameInfo(gameIDNum):
    requestString='http://store.steampowered.com/app/'+str(gameIDNum)+'/'

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

    print (str(gamePrice).strip())

def printGameInfoFromFullLink(gameLink):
    res = requests.get(gameLink, cookies=cookies)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'html.parser')
    gamePrice=soup.find(class_="price")
    if gamePrice==None:
        gamePrice=soup.find(class_="discount_final_price").string
        gamePrice=gamePrice+' on sale'
    else: gamePrice=gamePrice.string
    gameName=soup.find(class_="apphub_AppName").string
    print (gameName.encode('utf8'))

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
    userInput=input('Enter Game Name: ')

    formattedInput=formatUserInput(userInput)


    requestString='http://store.steampowered.com/search/?snr=1_4_4__12&term='+formattedInput
    res = requests.get(requestString)
    soup = BeautifulSoup(res.text, 'html.parser')

    firstlink=soup.find(class_='search_result_row')
    firstLinkContents=str(firstlink.get('href'))

    printGameInfoFromFullLink(firstLinkContents)




#printGameInfo(608800)
#printGameInfo(374320)
#printGameInfo(403640)
running=True
while(running):
    gameSearch()
