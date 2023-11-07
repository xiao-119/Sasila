class BaseDownLoader(object):
    def __init__(self):
        self.loginer = None

    def download(self, request):
        pass

    def set_loginer(self, loginer):
        self.loginer = loginer
