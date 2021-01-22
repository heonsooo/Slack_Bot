from slacker import Slacker
from bs4 import BeautifulSoup
import requests

# 기상청 오늘 날씨, 기온 스크래핑 
def weather_today():
    url ='https://weather.naver.com/'
    res=requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'html.parser')
    weather = soup.find_all("span", attrs={"class":"weather before_slash"})[0].text
    weather1 = soup.find_all("div", attrs={"class":"weather_area"})[0].text.replace('  ','').replace('\n','/').split('/')
    return weather1[1][5:]+' '+weather

# 알림 봇 
slack = Slacker('Code') 

# 메세지 전송
slack.chat.post_message('#알림_', '오늘도 좋은 아침! ')
slack.chat.post_message('#알림_', '오늘 날씨: ' + weather_today())
