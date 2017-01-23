# scrapy-proxymesh

Proxymesh downloader middleware for Scrapy.

## Installation

##### From PyPi

    pip install scrapy-proxymesh
    
##### From GitHub

    pip install -e git+https://github.com/mizhgun/scrapy-proxymesh@master#egg=scproxymesh

## Usage

settings.py:

    DOWNLOADER_MIDDLEWARES = {
        'scproxymesh.SimpleProxymeshMiddleware': 100,
    }
    
    PROXYMESH_URL = 'http://us-il.proxymesh.com:31280'
    
    # Proxymesh request timeout
    PROXYMESH_TIMEOUT = 60

