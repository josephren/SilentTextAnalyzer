__author__ = 'renwang.rw'

def find_index(line,pattern,num):
    index = -1
    count = 0
    while count < num:
        index += 1
        index = line.find(pattern,index)
        if index == -1:                 return index
        count += 1

    return index

