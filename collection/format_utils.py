# coding=utf-8
import os
from string.regular import find_index

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

def trim_a_directory(in_dir):
    ##change the last name
    changed_name_suffix = "trim"

    for in_name in os.listdir(in_dir):
        if not in_dir.endswith("/"):
            in_dir = in_dir + "/"

        if in_name.endswith(changed_name_suffix):      continue
        in_name = in_dir + in_name
        out_name = in_name +  "_" + changed_name_suffix
        out_file = open(out_name,'wb')
        for line in open(in_name):
        #This is the changed pleasejjj
            # begin = find_index(line,'"',3) + 1
            # line = line[begin:]

            # if not line.endswith("\n"):
            #     line += "\n"
            out_file.write(line)
        os.remove(in_name)
        out_file.close()

if __name__ == "__main__":
    direcotry = "d:/data/time_series"
    trim_a_directory(direcotry)
