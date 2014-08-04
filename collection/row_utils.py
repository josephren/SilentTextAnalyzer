# coding=utf-8
__author__ = 'renwang.rw'
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

if __name__ == "__main__":
    print get_row_number("realdata/freq_count/ivr_non_risk.csv")
