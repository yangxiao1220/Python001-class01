import scrapy


class MaoyanItem(scrapy.Item):
    # 电影名称、电影类型和上映时间
    item_name = scrapy.Field()
    item_type = scrapy.Field()
    item_time = scrapy.Field()
