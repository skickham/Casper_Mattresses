#CASPER ITEMS

import scrapy


class CasperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name        = scrapy.Field()
    age         = scrapy.Field()
    city        = scrapy.Field()
    state       = scrapy.Field()
    title       = scrapy.Field()
    review      = scrapy.Field()
    rating      = scrapy.Field()
    hours       = scrapy.Field()
    partners    = scrapy.Field()
    date        = scrapy.Field()
    verified    = scrapy.Field()
    page        = scrapy.Field()


