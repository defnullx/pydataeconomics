from datetime import datetime
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
        tableheader = '//div[@id="ctl00_ContentPlaceHolder1_ctl02_UpdatePanel1"]//div[@class="panel panel-default"]//div[@class="table-responsive"]//table[@class="table table-hover table-heatmap"]//thead//tr//th'
        tablecountry = '//div[@id="ctl00_ContentPlaceHolder1_ctl02_UpdatePanel1"]//div[@class="panel panel-default"]//div[@class="table-responsive"]//table[@class="table table-hover table-heatmap"]//tr//td/a'
        tablevalues = '//div[@id="ctl00_ContentPlaceHolder1_ctl02_UpdatePanel1"]//div[@class="panel panel-default"]//div[@class="table-responsive"]//table[@class="table table-hover table-heatmap"]//tr'

        for sel in response.xpath(tableheader):
            dataheader = sel.xpath('normalize-space(.)').get()
            print("header: "+dataheader)

        for sel in response.xpath(tablecountry):
            datacountry = sel.xpath('normalize-space(.)').get()
            print("country: "+datacountry)

        for sel in response.xpath(tablevalues):
            #datavalues = sel.xpath('normalize-space(.)').get()
            last = sel.xpath('normalize-space(./td[2]/.)').get()
            previous = sel.xpath('normalize-space(./td[3]/.)').get()
            reference = sel.xpath('normalize-space(./td[4]/.)').extract_first(default="default_value")
            reference = str(reference)

            if reference == "":
                continue

            print("reference: "+reference)
            referencedatetime = datetime.strptime(reference, "%b/%y")  # 09/21/22
            print("referencedatetime: "+str(referencedatetime))
            referencedate, referencetime = str(referencedatetime).split(" ")
            print("referencedate: "+referencedate)
            
            referencedate = datetime.strptime(referencedate, "%Y-%m-%d")  # 09/21/22
            date_time = referencedate.strftime("%d/%m/%Y")
            print("referencedate_fixed: "+str(date_time))
            #rdate = referencedate.
            #datavalues = str(data1)+","+str(data2)+","+str(data3totime)
            
            #referencedate = datetime.strftime("%d/%m/%y")
            #print("referencedate: "+referencedate)
            #print("values: "+str(data1)+","+str(data2)+","+str(data3))
            #print("values: "+datavalues)

