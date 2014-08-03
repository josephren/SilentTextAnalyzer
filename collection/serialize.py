import operator

__author__ = 'renwang'

def write_dict(dict_name,out_name):
    sorted_list = sorted(dict_name.iteritems(),key=operator.itemgetter(1),reverse=True)
    out_file = open(out_name,'wb')
    for entry in sorted_list:
        out_file.write(entry[0] + "\t" + str(entry[1]) + "\n")
    out_file.close()

def read_list(in_name):
    key_list = []
    for line in open(in_name):
        key_list.append(line.strip())
    return key_list