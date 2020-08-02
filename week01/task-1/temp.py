import requests
from bs4 import BeautifulSoup as bs4
import pandas as pd

path = 'C:\\Users\\YX\\Desktop\\maoyan.html'
htmlfile = open(path, 'r', encoding='utf-8')
htmlhandle = htmlfile.read()

url = 'https://maoyan.com/films?showType=3'

soup = bs4(htmlhandle,'html.parser')

html = soup.find_all('div',attrs={'class':"movie-item film-channel"})
list = []
for i in range(0,10):
    date = html[i].find_all('div',attrs={'class':"movie-hover-title"})
    name = html[i].find('span',attrs={'class':"name"}).text
    type = date[1].text[4:].strip()
    time = date[3].text[6:].strip()
    list.append([name,type,time])
moviel = pd.DataFrame(data = list)
moviel.to_csv('./movie1.csv',encoding='gbk',index=False,header=['m_name','m_type','m_time'])