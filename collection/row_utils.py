# coding=utf-8
__author__ = 'renwang.rw'
'''
Input is a row of keyword seperated by ','
such as, 'hello,love,you,all'
'''
def row_to_line(in_name,out_name,delimiter = ','):
    out_file = open(out_name,'wb')
    tokens = open(in_name).readline().strip().split(delimiter)
    for token in tokens:
        out_file.write(token + "\n")
    out_file.close()

def get_row_number(in_name):
    count = 0
    for line in open(in_name):
        count += 1
    return count
'''
this could be used to get the stop word set
'''
def get_word_set(in_name):
    word_set = set()
    for line in open(in_name):
        for token in line.strip().split():
            word_set.add(token)
    return word_set

if __name__ == "__main__":
    word_set = get_word_set("testdata/application/time_series/key_word")
    for key in word_set:
        print key
