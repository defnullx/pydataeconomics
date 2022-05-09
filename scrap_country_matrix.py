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
        tablevalues =   '//div//table[@id="ctl00_ContentPlaceHolder1_ctl01_GridView1"]//tr/td'

        df = pd.DataFrame()

        dataheadervalue = "Country"
        xa=u'\xa0'
        for sel in response.xpath(tableheader):
            dataheader = str(sel.xpath('normalize-space(.)').get())
            
            if xa in dataheader:
                continue

            dataheadervalue = dataheadervalue+","+dataheader
            dataheaderlist = list(dataheadervalue.split(","))
            df = pd.DataFrame(columns=dataheaderlist)

        for sel in response.xpath(tablevalues):
            datavalues = str(sel.xpath('normalize-space(.)').get() or None)
            
            if xa in datavalues:
                continue
            
            if 'None' in datavalues:
                continue

            print(datavalues)
            #datalist = list(datalist.split(","))
            #dataseries = pd.Series(datalist, index=df.columns)
            #df = df.append(dataseries, ignore_index=True)


process = CrawlerProcess({
            'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
            })
process.crawl(scraptbl)
process.start() 

#df.to_csv(csvfile01, index=False)
