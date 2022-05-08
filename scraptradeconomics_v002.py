import pandas
import scrapy
from scrapy.http import TextResponse
from scrapy.http import HtmlResponse

csvfile01 = "tbl01"
csvfile02 = "tbl02"
csvfile03 = "tbl03"


class scraptbl(scrapy.Spider):
    name = "scraptbl"
    start_urls = [
        'https://tradingeconomics.com/country-list/interest-rate?continent=world']

    def parse(self, response):
        tablevalues = '//div[@id="ctl00_ContentPlaceHolder1_ctl02_UpdatePanel1"]//div[@class="panel panel-default"]//div[@class="table-responsive"]//table[@class="table table-hover table-heatmap"]//tr'
        for sel in response.xpath(tablevalues):
            data = sel.xpath('normalize-space(.)').get()
            #data1= data.replace(" ", ",")
            print(data)