class BaseProcessor:
    spider_id = None
    # start_requests = []
    rules = ()
    allowed_domains = []
    
    def __init__(self):
        self.start_requests = []
    
    def process(self, response):
        pass