from collection.serialize import write_dict

__author__ = 'renwang.rw'

def cal_chi(self_dict,other_dict,self_num,other_num,out_name=None):
    chi_dict = dict()
    for key in self_dict:
        a = self_dict[key]  #self_freq
        b = 0
        if key in other_dict:
            b = other_dict[key] #other_freq
        c = self_num  -  a # self_absent
        d = other_num - b #other_absent

        nominator = (a*d-b*c)**2 * (self_num + other_num)
        denominator = (a + b) * ( c + d ) * (a + c) * (b + d)
        if denominator == 0:
            continue
        value = 1.0 * nominator / denominator
        chi_dict[key] = value
        if out_name is not None:
            write_dict(chi_dict,out_name)
    return chi_dict