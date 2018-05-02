# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PlayerAvatarItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class HupuPlayerItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    salary = scrapy.Field()
    player_id = scrapy.Field()
    url = scrapy.Field()
