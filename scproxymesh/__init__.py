# -*- coding: utf-8 -*
__author__ = 'mizhgun@gmail.com'
from scrapy.exceptions import NotConfigured

class SimpleProxymeshMiddleware(object):
    def __init__(self, settings):
        if not settings.getbool('PROXYMESH_ENABLED', True):
            raise NotConfigured
        self.proxy = settings.get('PROXYMESH_URL', 'http://us-il.proxymesh.com:31280')
        self.timeout = settings.getint('PROXYMESH_TIMEOUT', 0)

    @classmethod
    def from_crawler(cls, crawler):
        o = cls(crawler.settings)
        return o

    def process_request(self, request, spider):
        if not request.meta.get('bypass_proxy', False) and request.meta.get('proxy') is None:
            request.meta['proxy'] = self.proxy
            if self.timeout and not request.headers.get('X-ProxyMesh-Timeout'):
                request.headers.update({'X-ProxyMesh-Timeout': self.timeout})
