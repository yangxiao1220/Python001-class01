import scrapy

from movieinfo.items import  MaoyanItem
from bs4 import BeautifulSoup as bs4

class MaoyanFilmSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['https://maoyan.com/']
    start_urls = ["https://maoyan.com/films?showType=3",]

    def parse(self, response):
        film = MaoyanItem()
        print(response.text)
        soup = bs4(response.text,'html.parser')
        html = soup.find_all('div',attrs={'class':"movie-item film-channel"})
        for i in range(0, 10):
            date = html[i].find_all('div', attrs={'class': "movie-hover-title"})
            name =  html[i].find('span', attrs={'class': "name"}).text
            type = date[1].text[4:].strip()
            time = date[3].text[6:].strip()
            item = MaoyanItem()
            item['item_name'] = name
            item['item_type'] = type
            item['item_time'] = time
            yield item

