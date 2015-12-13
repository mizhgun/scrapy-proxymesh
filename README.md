# scrapy-proxymesh

Proxymesh downloader middleware for Scrapy.

settings.py:

    DOWNLOADER_MIDDLEWARES = {
        'scproxymesh.SimpleProxymeshMiddleware': 100,
    }
    
    PROXYMESH_URL = 'http://us-il.proxymesh.com:31280'
    
    # Proxymesh request timeout
    PROXYMESH_TIMEOUT = 60

