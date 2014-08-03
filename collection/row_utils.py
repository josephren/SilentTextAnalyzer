# coding=utf-8
__author__ = 'renwang.rw'
def row_to_line(in_name,out_name,delimiter = ','):
    out_file = open(out_name,'wb')
    tokens = open(in_name).readline().strip().split(delimiter)
    for token in tokens:
        out_file.write(token + "\n")
    out_file.close()

if __name__ == "__main__":
    row_to_line("realdata/freq_count/keyword","realdata/freq_count/keyword_row",delimiter="、")
