# coding=utf-8
from string.tries import Tries
from collection.serialize import read_list,write_dict
__author__ = 'renwang.rw'
in_file_name = "realdata/freq_count/ivr_non_risk.csv"
out_file_name = in_file_name + "_result"
pattern_name = "realdata/freq_count/keyword_row"
pattern_list =  read_list(pattern_name)
pattern_dict = {}
tries = Tries()
tries.put_list(pattern_list)
for token in pattern_list:
    pattern_dict[token] = 0

for line in open(in_file_name):
    result = tries.search_line(line)
    for token in result:
        pattern_dict[token] += 1

write_dict(pattern_dict,out_file_name)
