# coding=utf-8
__author__ = 'renwang'

R = 256

class Tries:
    def __init__(self):
        self.root = Node()
    def put_list(self,key_list):
        for key in key_list:
            self.put(key,key)
    def put(self,key,val):
        self.val = None
        self.put_recursive(self.root,key,val,0)
    def put_recursive(self,node,key,val,d):
        if node is None:
            node = Node()

        if len(key) == d :
            node.val = val
            return node

        index = ord(key[d:d+1])

        node.arr[index] = self.put_recursive(node.arr[index],key,val,d+1)
        return node

    def get(self,key):
        node = self.get_recursive(self.root,key,0)
        if node is None:                        return node
        return node.val

    def get_recursive(self,node,key,d):
        if node is None:                        return node
        if len(key) == d:                       return node

        index = ord(key[d:d+1])
        return self.get_recursive(node.arr[index],key,d+1)

    def search_line(self,line):
        M = len(line)
        i = 0
        match_list = []
        while i < M:
            j = 0
            node = self.root
            match_str = None
            while True:
                if node is None:            break
                if node.val is not None:
                    match_str = node.val
                    break
                if i + j == M:
                    break
                index = ord(line[i+j:i+j+1])
                node = node.arr[index]
                j += 1
            if match_str is None:
                i += 1
            else:
                i += len(match_str)
                match_list.append(match_str)
        return match_list
class Node:
    def __init__(self):
        self.arr = [None] * 256
        self.val = None

if __name__ == "__main__":
    tries = Tries()
    key_list = ['中国','我爱','安全']
    tries.put_list(key_list)
    key_list = tries.search_line("我爱我很喜欢我爱中国我也爱安全a")
    for key in key_list:
        print key
