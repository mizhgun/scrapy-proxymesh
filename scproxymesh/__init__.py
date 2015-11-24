# -*- coding: utf-8 -*
__author__ = 'mizhgun@gmail.com'


class SimpleProxymeshMiddleware(object):
    def __init__(self, settings):
        self.proxy = settings.get('PROXYMESH_URL', 'http://us-il.proxymesh.com:31280')

    @classmethod
    def from_crawler(cls, crawler):
        o = cls(crawler.settings)
        return o

    def process_request(self, request, spider):
        if request.meta.get('proxy') is None:
            request.meta['proxy'] = self.proxy
