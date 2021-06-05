# -*- coding: utf-8 -*-

# Define here the loaders for your items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/loaders.html

import re

from itemloaders.processors import TakeFirst
from scrapy.loader import ItemLoader

from weatherbot.items import WeatherBotItem


class WeatherBotItemLoader(ItemLoader):
    default_item_class = WeatherBotItem
    default_output_processor = TakeFirst()
