# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pandas

class MaoyanPipeline:

    def process_item(self, item, spider):
        maoyan_list = []
        maoyan_list.append((item['item_name'], item['item_type'], item['item_time']))
        work02_movie = pandas.DataFrame(data=maoyan_list)
        work02_movie.to_csv('./movies1.csv', encoding='gbk', mode='a', index=False, header=False)
        print(maoyan_list)
        return item
