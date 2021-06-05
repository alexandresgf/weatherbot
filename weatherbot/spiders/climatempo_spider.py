import scrapy
from scrapy import Request
from weatherbot.loaders import WeatherBotItemLoader
from weatherbot.settings import logger


class ClimaTempoSpider(scrapy.Spider):
    """
    This spider crawls the ClimaTempo website.
    """
    name = 'climatempo'

    def __init__(self, *args, **kwargs):
        super(ClimaTempoSpider, self).__init__(*args, **kwargs)
        self.start_urls = ['https://www.climatempo.com.br/previsao-do-tempo']
        self.allowed_domains = ['climatempo.com.br']

    def parse(self, response):
        for url in response.xpath('//ul[@class="list-cities"]//li//a/@href').getall():
            logger.debug('Accessing %s...' % response.urljoin(url))
            yield Request(url=response.urljoin(url), callback=self.parse_weather)

    def parse_weather(self, response):
        logger.debug('Starting to extract %s...' % response.url)

        loader = WeatherBotItemLoader(response=response)
        loader.add_xpath(
            'city', '//*[@id="mainContent"]/div[7]/div[4]/div[1]/div[2]/div[1]/div/div[1]/h1/text()', re='\nTempo\sagora\sem\s(\w+),')
        loader.add_xpath(
            'state', '//*[@id="mainContent"]/div[7]/div[4]/div[1]/div[2]/div[1]/div/div[1]/h1/text()', re='\nTempo\sagora\sem\s\w+,\s(\w+)\s')
        loader.add_xpath(
            'temperature', '//*[@id="mainContent"]/div[7]/div[4]/div[1]/div[2]/div[1]/div/div[2]/span/text()', re='\n(\w+)\n')
        loader.add_xpath(
            'climate_status', '//*[@id="mainContent"]/div[7]/div[4]/div[1]/div[2]/div[1]/div/div[3]/span[1]/text()')
        loader.add_xpath(
            'sensation', '//*[@id="mainContent"]/div[7]/div[4]/div[1]/div[2]/div[1]/div/div[3]/span[2]/text()', re='Sensação\s-\s(.+)')
        loader.add_xpath(
            'wind_velocity', '//*[@id="mainContent"]/div[7]/div[4]/div[1]/div[2]/div[1]/div/div[4]/ul/li[1]/div[2]/text()', re='SE\s-\s(.+)')
        loader.add_xpath(
            'humidity', '//*[@id="mainContent"]/div[7]/div[4]/div[1]/div[2]/div[1]/div/div[4]/ul/li[2]/div[2]/p/span/text()')
        loader.add_xpath(
            'pressure', '//*[@id="mainContent"]/div[7]/div[4]/div[1]/div[2]/div[1]/div/div[4]/ul/li[3]/div[2]/span/text()')

        yield loader.load_item()
