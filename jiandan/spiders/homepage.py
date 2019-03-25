import scrapy
from jiandan.items import JiandanArticleItem


class JiandanHomeSpider(scrapy.Spider):
    """首页爬虫"""
    custom_settings = {
        "ITEM_PIPELINES": {'jiandan.pipelines.JiandanArticlePipeline': 300}
    }
    name = "jiandan_home"
    allowed_domains = ['jandan.net']
    start_urls = ['https://jandan.net']

    def parse(self, response):
        article_list = response.css("div.thumbs_b")
        for article in article_list:
            jump_url = article.xpath("a/@href").extract()[0]

            print(jump_url)
            yield scrapy.Request(
                url=jump_url,
                callback=self.article_page
            )

    def article_page(self, response):
        title = response.css("h1").xpath("a/text()").extract()[1]
        content = response.xpath('//*[@id="content"]/div[2]/p/text()').extract()
        if len(content) >= 5:
            item = JiandanArticleItem()
            item["title"] = title
            item["content"] = content
            item["article_url"] = response.url
            yield item


if __name__ == '__main__':
    from scrapy import cmdline

    cmdline.execute("scrapy crawl jiandan_home".split())
