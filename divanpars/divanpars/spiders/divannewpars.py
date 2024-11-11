import scrapy


class DivannewparsSpider(scrapy.Spider):
    name = "divannewpars"
    allowed_domains = ["https://divan.ru"]
    start_urls = ["https://divan.ru/category/svet"]

    def parse(self, response):
        svets = response.css('div._Ud0k')
        for svet in svets:
            yield {
                'name' : svet.css('div.lsooF span::text').get(),
                'price' : svet.css('div.pY3d2 span::text').get(),
                'url' : svet.css('a').attrib['href']
            }


    # def parse(self, response):
    #     divans = response.css('div._Ud0k')
    #     for divan in divans:
    #         yield {
    #             'name' : divan.css('div.lsooF span::text').get(),
    #             'price' : divan.css('div.pY3d2 span::text').get(),
    #             'url' : divan.css('a').attrib['href']
    #         }
