# -*- coding: utf-8 -*-
import scrapy
import pandas as pd
# encoding=utf8
import sys
import csv
import re
#reload(sys)
#sys.setdefaultencoding('utf8')
import importlib
importlib.reload(sys)
from url_gumtree.items import UrlGumtreeItem
import random
#-------------------------------------------------------
#from bs4 import BeautifulSoup
class ExampleSpider(scrapy.Spider):
    name = 'gumtree_url04_12'
    #allowed_domains = ['example.com']
   # custom_settings = {'LOG_FILE': r'./abritel1.log','LOG_LEVEL':'ERROR'}
    start_urls = ["https://www.gumtree.co.za"]

    def parse(self, response):
        list_url=list(pd.read_csv("gumtree_filtre.csv")['url'])
        #list_url=["https://www.gumtree.co.za/s-cars-bakkies/v1c9077p1"] 
        print(list_url)
        for commune in list_url:
            print(commune)
            req = scrapy.Request(commune,callback=self.parsegum)
            print(req)
            yield req

    def parsegum(self, response):
        print("-------------------------------------------------------------")
        print(response)
        base_url="https://www.gumtree.co.za"
        liste=response.xpath("//a[@class='related-ad-title']/@href").extract()
        count=response.xpath("//span[@class='ads-count']/text()").extract_first()
        print(count)
        if len(liste)>0:   
            #count=response.xpath("//span[@class='ads-count']/text()").extract_first()
            nb_reg=re.compile("\d+")
            count = nb_reg.findall(count)[0]
            print(count)
            if int(count) > 1000:
                with open('csvfile3.csv','a', newline='') as f:
                    thewriter = csv.writer(response.url)
                    thewriter.writerow([str(count)])
            print(liste)
            #if "status=adInactive" in liste:
            #    pass        
            print("*********************",str(response))

            for announce in liste:
                itm=UrlGumtreeItem()
                announce=base_url+str(announce)
                #print(announce,"---------------------")
                if "status=adInactive" in liste:
                    pass 
                else:
                    #yield scrapy.Request(url=announce,callback=self.parse,dont_filter=True)
                    itm['url']=announce
                    print(itm)
                    yield itm
            print("ok")

            #next_page=response.xpath("//a[@class='next follows']/@href").extract_first()
            next_page=response.xpath("//div[@id='pagination']/div/span/a[@class=' icon-pagination-right']/@href").extract_first()
            print("next page ",next_page)
            if "page-" in response.url:
                print("ffffffffffffffffffffffffff",next_page)
                #next_page=response.xpath("//span[@class='pag-box']/a/@href").extract_first()
                #next_page=response.xpath("//a[@class='icon-pagination-right']/a/@href").extract_first()
                next_page=response.xpath("//div[@id='pagination']/div/span/a[@class=' icon-pagination-right']/@href").extract_first()
            if next_page is not None:
                next_page=base_url+next_page
                print(next_page)
                next_page_link = response.urljoin(next_page)
                print("oooo",next_page_link)
                yield scrapy.Request(url=next_page_link,callback=self.parsegum)
        



