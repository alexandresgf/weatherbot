# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from datetime import datetime
from time import time

from pymongo import MongoClient

from weatherbot.settings import logger


class CheckFieldsPipeline(object):
    """
    Check if the item has all fields set
    """

    def process_item(self, item, spider):
        if not [f for f in item.fields if not item.get(f)]:
            return item

        return None


class MongoDBPipeline(object):
    """
    Save the extracted items
    """
    collection_name = 'cities'

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGODB_CONN_URI'),
            mongo_db=crawler.settings.get('MONGODB_DB_NAME')
        )

    def open_spider(self, spider):
        self.client = MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        if item:
            self.db[self.collection_name].update_one(
                {
                    'city': item.get('city'),
                    'state': item.get('state')
                },
                {
                    '$setOnInsert': {
                        'city': item.get('city'),
                        'state': item.get('state')
                    },
                    '$set': {
                        'temperature': item.get('temperature'),
                        'climateStatus': item.get('climate_status'),
                        'sensation': item.get('sensation'),
                        'windVelocity': item.get('wind_velocity'),
                        'humidity': item.get('humidity'),
                        'pressure': item.get('pressure'),
                        'verifiedAt': datetime.utcfromtimestamp(time())
                    }
                },
                upsert=True
            )

            logger.info('Verified the weather of %s, %s successfully' %
                        (item.get('city'), item.get('state')))

        return item
