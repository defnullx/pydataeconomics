from IPython.display import display
import pandas as pd
import scrapy
from scrapy.crawler import CrawlerProcess


csvfile01 = "country_matrix_world.csv"

class scraptbl(scrapy.Spider):
    name = "countrymatrix"
    start_urls = [
        'https://tradingeconomics.com/matrix']

    def parse(self, response):
        tableheader =   '//div//table[@id="ctl00_ContentPlaceHolder1_ctl01_GridView1"]//thead//tr//th'
        tablevalues =   '//div//table[@id="ctl00_ContentPlaceHolder1_ctl01_GridView1"]//tr//td'

        df = pd.DataFrame()

        xa=u'\xa0'
        dataheadervalue = "Country"
        for sel in response.xpath(tableheader):
            dataheader = str(sel.xpath('normalize-space(.)').get(default=""))
            if xa in dataheader:
                continue

            dataheadervalue = dataheadervalue+","+dataheader
            dataheaderlist = list(dataheadervalue.split(","))
            df = pd.DataFrame(columns=dataheaderlist)


        i = 0
        datavalues = ""
        for sel in response.xpath(tablevalues):
            datavalue = str(sel.xpath('normalize-space(.)').get(default=""))
            if xa in datavalue:
                continue

            datavalues = datavalues+"#"+datavalue

            i += 1
            if i == 12:
                datavalues = datavalues[1:]
                datavalueslist = list(datavalues.split("#"))
                dataseries = pd.Series(datavalueslist, index=df.columns)
                df = df.append(dataseries, ignore_index=True)
                datavalues = ""
                i = 0

        display(df)
        df.to_csv(csvfile01, index=False)


process = CrawlerProcess({
            'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
            })
process.crawl(scraptbl)
process.start() 


