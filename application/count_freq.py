# coding=utf-8
from string.tries import Tries

__author__ = 'renwang.rw'
in_file_name = "testdata/application/freq"
out_file_name = in_file_name + "_result"
pattern_list = ["小猫", "小狗","喜欢"]
pattern_dict = {}
tries = Tries()
tries.put_list(pattern_list)
for token in pattern_list:
    pattern_dict[token] = 0

for line in open(in_file_name):
    result = tries.search_line(line)
    for token in result:
        pattern_dict[token] += 1

out_file_path = open(out_file_name, 'wb')
for key in pattern_dict:
    out_file_path.write(key + '\t' + str(pattern_dict[key]) + '\n')
out_file_path.close()