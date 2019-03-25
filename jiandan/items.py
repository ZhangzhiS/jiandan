# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JiandanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class JiandanPicItem(scrapy.Item):
    """煎蛋无聊图"""
    # image_url = scrapy.Field()  # 图片链接
    # image_path = scrapy.Field()  # 图片链接
    image_urls = scrapy.Field()
    images = scrapy.Field()
    image_paths = scrapy.Field()


class JiandanArticleItem(scrapy.Item):
    """文章"""
    title = scrapy.Field()
    article_url = scrapy.Field()
    content = scrapy.Field()
