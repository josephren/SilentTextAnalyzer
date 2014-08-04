import operator

__author__ = 'renwang'

def write_dict(dict_instance,out_name):
    sorted_list = sorted(dict_instance.iteritems(),key=operator.itemgetter(1),reverse=True)
    out_file = open(out_name,'wb')
    for entry in sorted_list:
        out_file.write(entry[0] + "\t" + str(entry[1]) + "\n")
    out_file.close()

def read_dict(in_name):
    in_dict = {}
    for line in open(in_name):
        tokens = line.strip().split("\t")
        in_dict[tokens[0]] = float(tokens[1])
    return in_dict

def read_list(in_name):
    key_list = []
    for line in open(in_name):
        key_list.append(line.strip())
    return key_list

if __name__ == "__main__":
    in_dict = read_dict('realdata/freq_count/risk_freq')
    for key in in_dict:
        print key,in_dict[key]