#! python3 

import bs4, requests 


weatherSite = requests.get('https://weather.com/en-CA/weather/today/l/eef019cb4dca2160f08eb9714e30f28e05e624bbae351ccb6a855dbc7f14f017')
weatherSoup = bs4.BeautifulSoup(weatherSite.text, 'html.parser')


weatherLoc = weatherSoup.select('h1[class*="CurrentConditions--location--"]')
weatherTime = weatherSoup.select('div[class*="CurrentConditions--timestamp--"]')
weatherTemp = weatherSoup.select('span[class*="CurrentConditions--tempValue--"]')
weatherCondition = weatherSoup.select('div[class*="CurrentConditions--phraseValue--"]')

if weatherSoup.find_all("div", "CurrentConditions--precipValue--"):
    weatherDet = weatherSoup.select('div[class*="CurrentConditions--precipValue--"] > span:nth-child(1)')
    det = weatherDet[0].text

location = weatherLoc[0].text
time = weatherTime[0].text
temp = weatherTemp[0].text
condition = weatherCondition[0].text


print(location)
print(time)
print(temp + 'C')
print(condition)

if weatherSoup.find_all("div", "CurrentConditions--precipValue--"):     
    print(det)
