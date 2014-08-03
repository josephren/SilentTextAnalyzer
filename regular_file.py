# coding=utf-8
import re

__author__ = 'renwang'

def replace(input_path,output_path,pattern,sub_pattern):
    output_file = open(output_path,'wb')
    pattern_instance = re.compile(pattern)
    for line in open(input_path):
        sub_line = pattern_instance.sub(sub_pattern,line)
        output_file.write(sub_line)
    output_file.close()

input_path = "/Users/renwang/Documents/百度云同步盘/work/data/sentiment/0620_0624_null.csvseg"
output_path =input_path  + "remove"
pattern = '"(\s*\d*\s*" ,)|"'
sub_pattern = ""
replace(input_path,output_path,pattern,sub_pattern)