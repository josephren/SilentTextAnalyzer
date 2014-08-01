__author__ = 'renwang'

class RabinKarp:
    def __init__(self,pattern):
        self.R = 256
        self.Q = 997
        self.pattern = pattern