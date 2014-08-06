import os

__author__ = 'renwang'

def change_to_utf(in_name,out_name):
    out_file = open(out_name,'wb')
    for line in open(in_name):
        out_file.write(line.decode('gbk').encode('utf-8'))
    out_file.close()

if __name__ == "__main__":
    for in_name in os.listdir('realdata/application/time_series/06/'):
        in_name = 'realdata/application/time_series/06/' + in_name
        os.rename(in_name,in_name[:-3])