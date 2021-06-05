# -*- coding: utf-8 -*-

# Define here the processors for your items loaders
#
# See: https://docs.scrapy.org/en/latest/topics/loaders.html#input-and-output-processors

def default_processor(self, values):
    """
    This is an example of processor, please remove it or rename the function
    and refactor its behavior.
    """
    for value in values:
        yield value.lower()
