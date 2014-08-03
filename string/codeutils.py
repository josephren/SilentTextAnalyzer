__author__ = 'renwang'

def change_to_utf(in_name,out_name):
    out_file = open(out_name,'wb')
    for line in open(in_name):
        out_file.write(line.decode('gbk').encode('utf-8'))
    out_file.close()
