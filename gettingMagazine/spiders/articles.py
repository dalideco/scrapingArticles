import scrapy

class ArticlesSpider(scrapy.Spider):
    name = "articles"

    start_url ='http://www.laughfactory.com/magazine/'


    def start_requests(self):
        yield scrapy.Request(url=start_url, callback=self.parse_front)

    def parse_front(self, response):
        
        for joke in response.xpath('//div[@class="magazine-detail-content"]'):
            yield {
                'joke_text': joke.xpath('.//div[@class="magazine-sec-description"]/p/text()').extract_first()
            }
        
        next_page = response.xpath('//li[@class="next"]/a/@href').extract_first()
        
        if next_page is not None:
            next_page_link=response.urljoin(next_page)
            yield scrapy.Request(url=next_page_link, callback=self.parse_front)

