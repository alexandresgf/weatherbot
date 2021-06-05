# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WeatherBotItem(scrapy.Item):
    city = scrapy.Field()
    state = scrapy.Field()
    temperature = scrapy.Field()
    climate_status = scrapy.Field()
    sensation = scrapy.Field()
    wind_velocity = scrapy.Field()
    humidity = scrapy.Field()
    pressure = scrapy.Field()
