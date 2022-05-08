import scrapy
from scrapy.http import TextResponse
from scrapy.http import HtmlResponse

csvfile01 = "tbl01"
csvfile02 = "tbl02"
csvfile03 = "tbl03"

class scraptbl(scrapy.Spider):
    name = "scraptbl"
    start_urls = ['https://tradingeconomics.com/country-list/interest-rate?continent=world']

    def parse(self, response):
        #link = response.xpath('//a[contains(@class, "next-posts-link")]/a/@href').get()  # extract using class
        #response.xpath('')
        for sel in response.xpath('//div[@id="ctl00_ContentPlaceHolder1_ctl02_UpdatePanel1"]//div[@class="panel panel-default"]//div[@class="table-responsive"]//table[@class="table table-hover table-heatmap"]//tr//td/a'):
            country = sel.xpath('@href').get()
            print(country)

        for sel in response.xpath('//div[@id="ctl00_ContentPlaceHolder1_ctl02_UpdatePanel1"]//div[@class="panel panel-default"]//div[@class="table-responsive"]//table[@class="table table-hover table-heatmap"]//tr//td/span'):
            data = sel.xpath('text()').get() 
            print("dados: "+data)
           


