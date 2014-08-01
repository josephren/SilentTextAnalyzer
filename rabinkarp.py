__author__ = 'renwang'

class RabinKarp:
    def __init__(self,pattern):
        self.R = 256
        self.Q = 997
        self.pattern = pattern
    def hash(self,word):
        hash = 0
        for i in range(len(word)):
            hash = (hash * self.R + ord(word[i:i+1])) % self.Q
        return hash

if __name__ == "__main__":
    rb = RabinKarp("hello")
    print rb.hash("hello")