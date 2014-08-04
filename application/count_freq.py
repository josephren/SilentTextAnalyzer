# coding=utf-8
from statistics.chi_square import cal_chi
from string.tries import Tries
from collection.serialize import read_list,write_dict, read_dict

__author__ = 'renwang.rw'

def freq_file():
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

risk_dict = read_dict("realdata/freq_count/risk_freq")
non_risk_dict = read_dict("realdata/freq_count/non_risk_freq")
risk_number = 144760.0
non_risk_number = 2426303.0
out_file = "realdata/freq_count/p_result"
cal_chi(risk_dict,non_risk_dict,risk_number,non_risk_number,out_file)
