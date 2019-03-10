# 煎蛋爬虫

- 2019-03-10
    
    爬取煎蛋无聊图的最新一页的图片下载到本地，使用了scrapy自带的中间件ImagesPipeline。
    
    ImagesPipeline的特点：
    - 将下载图片转换成通用的JPG和RGB格式
    - 避免重复下载
    - 缩略图生成
    - 图片大小过滤
