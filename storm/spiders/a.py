import scrapy
from scrapy import Selector
from scrapy_playwright.page import PageMethod
from scrapy_playwright import page
from scrapy_playwright.page import PageMethod
from storm.read_data import codes
from storm.read_data import volts
import requests

class ASpider(scrapy.Spider):
    name = "a"
    


    def start_requests(self):


        for code in codes :
               for volt in volts :
                   
                   

                   if code == 70378 :
                    yield scrapy.Request(
                url="https://www.check24.de/strom/vergleich/check24/",dont_filter=True,
                callback=self.parse1,
                meta=dict(
                playwright = True,
                playwright_include_page = True ,
                playwright_page_methods = [
                    PageMethod('click', selector="//html/body/div[2]/div[1]/div[3]/a[2]"),
                    PageMethod('fill', selector='//*[@id="zipcode"]',value=f'{code}'),
                    PageMethod('click', selector='//*[@id="resultForm"]/div[1]/div/div[3]/div/div[2]/div[1]/div[1]'),
                    PageMethod('click', selector='//*[@id="city"]'),
                    PageMethod('select_option',selector='//*[@id="city"]',value='Stuttgart'),   #
                    PageMethod('fill', selector='//*[@id="totalconsumption"]',value=f'{volt}'),    #
                    PageMethod('click', selector='//*[@id="pricecap_no"]/div'),
                    PageMethod('click', selector='//*[@id="pricing_year"]/div'),
                    PageMethod('click', selector='//*[@id="filter_setting_all"]/div[1]'),
                    PageMethod('click', selector='//*[@id="resultForm"]/div[1]/div/div[4]/div[2]/div[3]/div[2]/div[3]/div[2]/label'),
                    PageMethod('click', selector='//*[@id="contractperiod_12"]/div'),
                    PageMethod('click', selector='//*[@id="consider_max_bonus_share_yes"]'),                   
                ],
                errback =self.errback 
            ))
                   elif code == 85540 :
                    yield scrapy.Request(
                url="https://www.check24.de/strom/vergleich/check24/",dont_filter=True,
                callback=self.parse1,
                meta=dict(
                playwright = True,
                playwright_include_page = True ,
                playwright_page_methods = [
                    PageMethod('click', selector="//html/body/div[2]/div[1]/div[3]/a[2]"),
                    PageMethod('fill', selector='//*[@id="zipcode"]',value=f'{code}'),
                    PageMethod('click', selector='//*[@id="resultForm"]/div[1]/div/div[3]/div/div[2]/div[1]/div[1]'),
                    PageMethod('click', selector='//*[@id="city"]'),
                    PageMethod('select_option',selector='//*[@id="city"]',value='München'),   #
                    PageMethod('fill', selector='//*[@id="totalconsumption"]',value=f'{volt}'),    #
                    PageMethod('click', selector='//*[@id="pricecap_no"]/div'),
                    PageMethod('click', selector='//*[@id="pricing_year"]/div'),
                    PageMethod('click', selector='//*[@id="filter_setting_all"]/div[1]'),
                    PageMethod('click', selector='//*[@id="resultForm"]/div[1]/div/div[4]/div[2]/div[3]/div[2]/div[3]/div[2]/label'),
                    PageMethod('click', selector='//*[@id="contractperiod_12"]/div'),
                    PageMethod('click', selector='//*[@id="consider_max_bonus_share_yes"]'),                   
                ],
                errback =self.errback 
            ))
                   elif code == 14109 :
                    yield scrapy.Request(
                url="https://www.check24.de/strom/vergleich/check24/",dont_filter=True,
                callback=self.parse1,
                meta=dict(
                playwright = True,
                playwright_include_page = True ,
                playwright_page_methods = [
                    PageMethod('click', selector="//html/body/div[2]/div[1]/div[3]/a[2]"),
                    PageMethod('fill', selector='//*[@id="zipcode"]',value=f'{code}'),
                    PageMethod('click', selector='//*[@id="resultForm"]/div[1]/div/div[3]/div/div[2]/div[1]/div[1]'),
                    PageMethod('click', selector='//*[@id="city"]'),
                    PageMethod('select_option',selector='//*[@id="city"]',value='Berlin'),   #
                    PageMethod('fill', selector='//*[@id="totalconsumption"]',value=f'{volt}'),    #
                    PageMethod('click', selector='//*[@id="pricecap_no"]/div'),
                    PageMethod('click', selector='//*[@id="pricing_year"]/div'),
                    PageMethod('click', selector='//*[@id="filter_setting_all"]/div[1]'),
                    PageMethod('click', selector='//*[@id="resultForm"]/div[1]/div/div[4]/div[2]/div[3]/div[2]/div[3]/div[2]/label'),
                    PageMethod('click', selector='//*[@id="contractperiod_12"]/div'),
                    PageMethod('click', selector='//*[@id="consider_max_bonus_share_yes"]'),                   
                ],
                errback =self.errback 
            ))
                   elif code == 15236 :
                    yield scrapy.Request(
                url="https://www.check24.de/strom/vergleich/check24/",dont_filter=True,
                callback=self.parse1,
                meta=dict(
                playwright = True,
                playwright_include_page = True ,
                playwright_page_methods = [
                    PageMethod('click', selector="//html/body/div[2]/div[1]/div[3]/a[2]"),
                    PageMethod('fill', selector='//*[@id="zipcode"]',value=f'{code}'),
                    PageMethod('click', selector='//*[@id="resultForm"]/div[1]/div/div[3]/div/div[2]/div[1]/div[1]'),
                    PageMethod('click', selector='//*[@id="city"]'),
                    PageMethod('select_option',selector='//*[@id="city"]',value='Frankfurt'),   #
                    PageMethod('fill', selector='//*[@id="totalconsumption"]',value=f'{volt}'),    #
                    PageMethod('click', selector='//*[@id="pricecap_no"]/div'),
                    PageMethod('click', selector='//*[@id="pricing_year"]/div'),
                    PageMethod('click', selector='//*[@id="filter_setting_all"]/div[1]'),
                    PageMethod('click', selector='//*[@id="resultForm"]/div[1]/div/div[4]/div[2]/div[3]/div[2]/div[3]/div[2]/label'),
                    PageMethod('click', selector='//*[@id="contractperiod_12"]/div'),
                    PageMethod('click', selector='//*[@id="consider_max_bonus_share_yes"]'),                   
                ],
                errback =self.errback 
            ))
                   elif code == 14480 :
                    yield scrapy.Request(
                url="https://www.check24.de/strom/vergleich/check24/",dont_filter=True,
                callback=self.parse1,
                meta=dict(
                playwright = True,
                playwright_include_page = True ,
                playwright_page_methods = [
                    PageMethod('click', selector="//html/body/div[2]/div[1]/div[3]/a[2]"),
                    PageMethod('fill', selector='//*[@id="zipcode"]',value=f'{code}'),
                    PageMethod('click', selector='//*[@id="resultForm"]/div[1]/div/div[3]/div/div[2]/div[1]/div[1]'),
                    PageMethod('click', selector='//*[@id="city"]'),
                    PageMethod('select_option',selector='//*[@id="city"]',value='Potsdam'),   #
                    PageMethod('fill', selector='//*[@id="totalconsumption"]',value=f'{volt}'),    #
                    PageMethod('click', selector='//*[@id="pricecap_no"]/div'),
                    PageMethod('click', selector='//*[@id="pricing_year"]/div'),
                    PageMethod('click', selector='//*[@id="filter_setting_all"]/div[1]'),
                    PageMethod('click', selector='//*[@id="resultForm"]/div[1]/div/div[4]/div[2]/div[3]/div[2]/div[3]/div[2]/label'),
                    PageMethod('click', selector='//*[@id="contractperiod_12"]/div'),
                    PageMethod('click', selector='//*[@id="consider_max_bonus_share_yes"]'),                   
                ],
                errback =self.errback 
            ))
                   else : pass

                



            

    
    async def parse1(self, response):

        page = response.meta["playwright_page"]
        page.set_default_timeout(10000)


        #page = response.meta["playwright_page"]

        n = response.css('.js-result-row')
        
        
        for i in range(1,len(n)):


            a = response.xpath(f'//div/div[1]/div[2]/div[2]/div[3]/div[4]/article[{i}]/div[1]/div/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/img/@alt').extract()
            if (a == ['stromee']) :
                print(i)
                await(page.locator(f'//div/div[1]/div[2]/div[2]/div[3]/div[4]/article[{i}]/div[1]/div/div[1]/div[2]/div[2]/div/div[1]/div')).click() 
                await(page.locator(f'//div/div[1]/div[2]/div[2]/div[3]/div[4]/article[{i}]/div[2]/div[2]/label[1]/div ')).click()
                
                await page.wait_for_timeout(90)
        content = await page.content()
        sel = Selector(text=content)  

        

        for i in range(1,len(n)):


            a = response.xpath(f'//div/div[1]/div[2]/div[2]/div[3]/div[4]/article[{i}]/div[1]/div/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/img/@alt').extract()
            if (a == ['stromee']) :
        
        
              b = sel.xpath(f'//*[@id="c24-content"]/div/div[1]/div[2]/div[2]/div[3]/div[4]/article[{i}]/div[2]/div[2]/div[1]/div/div[1]/div[1]/div/div[2]/text()').extract()
            
              c = sel.xpath(f'//*[@id="c24-content"]/div/div[1]/div[2]/div[2]/div[3]/div[4]/article[{i}]/div[1]/div/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/strong[1]/text()').extract()
                    
              d = sel.xpath(f'//*[@id="c24-content"]/div/div[1]/div[2]/div[2]/div[3]/div[4]/article[{i}]/div[1]/div/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/strong[2]/text()').extract()
    
              e = sel.xpath(f'//*[@id="c24-content"]/div/div[1]/div[2]/div[2]/div[3]/div[4]/article[{i}]/div[2]/div[2]/div[1]/div/div[1]/div[4]/div/div[2]/text()').extract()
              
              #f = datetime.now()
                       
              g = sel.xpath(f'//*[@id="c24-content"]/div/div[1]/div[2]/div[2]/div[3]/div[4]/article[{i}]/div[2]/div[2]/div[1]/div/div[1]/div[2]/div/div[2]/text()').extract()
                 
              h = response.xpath('//*[@id="resultForm"]/div[1]/div/div[2]/div/div/div[2]/div[2]/text()').extract()

              await page.close()


              yield {
                  
                  'brand'               : c + d ,         
                  'price'               : e ,
                  'city'        : h ,
                  'total consumption'   : g , 
                  'zip code'            : b ,
                  
              }
            
           

        


    async def errback(self,failure) :
        page = failure.request.meta["playwright_page"]
        await page.close()