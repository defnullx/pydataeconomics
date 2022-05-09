from IPython.display import display
import pandas as pd
from datetime import datetime
import scrapy
from scrapy.crawler import CrawlerProcess

csvfile01 = "inflation_rate.csv"

class scraptbl(scrapy.Spider):
    name = "inflationrate"
    start_urls = [
        'https://tradingeconomics.com/forecast/inflation-rate']

    def parse(self, response):
        tableheader =   '//div[@id="ctl00_ContentPlaceHolder1_ctl01_UpdatePanel1"]//thead'
        tablevalues =   '//div[@id="ctl00_ContentPlaceHolder1_ctl01_UpdatePanel1"]//tr'

        df = pd.DataFrame()

        xa=u'\xa0'
        for sel in response.xpath(tableheader):
            dataheader = str(sel.xpath('normalize-space(.)').get())

            dataheader = dataheader.replace("Last", "Last """)
            dataheader = dataheader[43:]
            dataheaderlist = list(dataheader.split(" "))
            df = pd.DataFrame(columns=dataheaderlist)

        for sel in response.xpath(tablevalues):
            datacountry = str(sel.xpath('normalize-space(./td/a/.)').get())
            last = str(sel.xpath('normalize-space(./td[2])').get())
            reference = str(sel.xpath('normalize-space(./td[3])').get())
            Q1 = str(sel.xpath('normalize-space(./td[4])').get())
            Q2 = str(sel.xpath('normalize-space(./td[5])').get())
            Q3 = str(sel.xpath('normalize-space(./td[6])').get())
            Q4 = str(sel.xpath('normalize-space(./td[7])').get())


            reference = str(reference)
            if reference == "":
                continue

            referencedatetime = datetime.strptime(reference, "%b/%y")
            referencedate, referencetime = str(referencedatetime).split(" ")
            referencedate = datetime.strptime(referencedate, "%Y-%m-%d")
            date_time = referencedate.strftime("%m/%d/%Y")

            datavalues = datacountry+"#"+last+"#"+date_time+"#"+Q1+"#"+Q2+"#"+Q3+"#"+Q4
            datavalueslist = list(datavalues.split("#"))
            dataseries = pd.Series(datavalueslist, index=df.columns)
            df = df.append(dataseries, ignore_index=True)

        display(df)
        df.to_csv(csvfile01, index=False)


process = CrawlerProcess({
            'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
            })
process.crawl(scraptbl)
process.start() 


