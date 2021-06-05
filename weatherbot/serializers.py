# -*- coding: utf-8 -*-

# Define here the serializers for your item fields
#
# See: https://docs.scrapy.org/en/latest/topics/exporters.html#declaring-a-serializer-in-the-field

def default_serializer(value):
    """
    This is an example of serializer, please remove it or rename the function
    and refactor its behavior.
    """
    return value.lower()
