BOT_NAME = 'annonce_gumtree'

SPIDER_MODULES = ['annonce_gumtree.spiders']
NEWSPIDER_MODULE = 'annonce_gumtree.spiders'

ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)

CONCURRENT_REQUESTS = 200

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 0.5
# The download delay setting will honor only one of:
CONCURRENT_REQUESTS_PER_DOMAIN = 8
CONCURRENT_REQUESTS_PER_IP = 8
#DOWNLOAD_TIMEOUT= 10000

RETRY_TIMES= 10
RETRY_HTTP_CODES = [500, 502, 503, 504, 408, 416,405,403,429,]#302,301,508]

DOWNLOADER_MIDDLEWARES = {
    'annonce_gumtree.middlewares.GumtreeSpiderMiddleware': 1,
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'scrapy_fake_useragent.middleware.RandomUserAgentMiddleware': 400,
    'scrapy.downloadermiddlewares.retry.RetryMiddleware': 901,


}

ITEM_PIPELINES = {
    'annonce_gumtree.pipelines.AnnonceGumtreePipeline': 300,
}

AUTOTHROTTLE_ENABLED = True
# The initial download delay
AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0

HTTPCACHE_ENABLED = True
HTTPCACHE_EXPIRATION_SECS = 1728000
HTTPCACHE_DIR = 'httpcache'
HTTPCACHE_IGNORE_HTTP_CODES = [500, 502, 503, 504, 408, 416,405,403,429,302,301,508,404,400]
HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

