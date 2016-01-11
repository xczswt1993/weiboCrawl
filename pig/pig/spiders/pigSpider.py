__author__ = 'stone'

from pig.items import  PigItem
from scrapy.spiders import Spider
from scrapy.selector import Selector

'''
price
//*[@id="page_list"]/ul/li[1]/div[2]/span[1]/i
//*[@id="page_list"]/ul/li[2]/div[2]/span[1]/i
//*[@id="page_list"]/ul/li[3]/div[2]/span[1]/i
title
//*[@id="page_list"]/ul/li[1]/div[2]/div/a/span
//*[@id="page_list"]/ul/li[2]/div[2]/div/a/span

hiddenTxt
//*[@id="page_list"]/ul/li[1]/div[2]/div/em
//*[@id="page_list"]/ul/li[2]/div[2]/div/em
'''


class PigSpider(Spider):
    name = 'pigSpider'
    allowed_domains = ['bj.xiaozhu.com']
    start_urls = ['http://bj.xiaozhu.com/search-duanzufang-p1-0/',
                  'http://bj.xiaozhu.com/search-duanzufang-p2-0/',
                  'http://bj.xiaozhu.com/search-duanzufang-p3-0/'
                ]

    def parse(self, response):
        sel = Selector(response)
        title = sel.xpath('//span[@class="result_title hiddenTxt"]')
        price = sel.xpath('//span[@class="result_price"]/i')
        hiddenTxt = sel.xpath('//em[@class="hiddenTxt"]')
        comment = sel.xpath('//span[@class="commenthref"]')
        items = []
        for title, price, hiddenTxt, comment in zip(title, price, hiddenTxt, comment):
            item = PigItem()
            item['title'] = title.xpath('text()').extract()[0]
            item['price'] = price.xpath('text()').extract()[0]
            item['type'] = "".join(hiddenTxt.xpath('text()').extract()[0].split())
            item['area'] = "".join(hiddenTxt.xpath("text()").extract()[-1].split()).split('-')[-1]
            item['comment'] = comment.xpath('text()').extract()[0]
            yield item




