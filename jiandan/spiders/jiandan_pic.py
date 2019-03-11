# -*- coding: utf-8 -*-
import base64

import scrapy

from jiandan.items import JiandanPicItem


class JiandanPicSpider(scrapy.Spider):
    name = 'jiandan_pic'
    allowed_domains = ['jandan.net/pic']
    start_urls = ['https://jandan.net/pic/', 'https://jandan.net/ooxx/']

    def parse(self, response):
        image_urls = []
        image_items = response.css("span.img-hash")  # //*[@id="comment-4172989"]/div/div/div[2]/p/img
        for i in image_items:
            encode_str = i.xpath("text()").extract()[0]
            image_url = decode_image_url(encode_str)
            print(image_url)
            image_urls.append(image_url)
        item = JiandanPicItem()
        item["image_urls"] = image_urls
        yield item
        # 执行翻页操作
        page_num = response.xpath('//*[@id="comments"]/div[3]/div/a/@href').extract()
        for next_page in page_num:
            next_page_url = "https://" + next_page
            print(next_page_url)
            yield scrapy.Request(url=next_page_url, callback=self.parse)


def decode_image_url(encode_str):
    """
    对编码之后的图片链接进行解码
    :param encode_str: 编码之后的字符串
    :return: 图片链接
    """
    image_url = base64.b64decode(encode_str).decode("utf-8")
    return "https:"+image_url
