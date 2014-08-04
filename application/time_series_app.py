import time
import sqlite3
from collection.row_utils import get_word_set
from string.tries import Tries

__author__ = 'renwang'


def from_str_to_timestamp(str_time):
    time_array = time.strptime(str_time,'%Y-%m-%d %H:%M:%S')
    time_stamp = int(time.mktime(time_array))
    return time_stamp


def from_timestamp_to_index(str_time,base_time,interval=60*5):
    time_stamp = from_str_to_timestamp(str_time)
    time_base = from_str_to_timestamp(base_time)
    return (time_stamp - time_base) / interval


class CountFreq:
    def __init__(self,key_in_name,doc_in_name,base_time):
        self.word_dict = {}
        self.freq_dict = {}
        self.tries = Tries()
        self.base_time = base_time
        key_list = list(get_word_set(key_in_name))
        self.tries.put_list(key_list)
        for line in open(doc_in_name):
            self.read_line(line)
        self.write_dict_to_db()

    def read_line(self,line):
        #to prevent the duplicate count of a certain term
        key_set = set()
        previous_index = -1
        for chat_record in line.strip().split("|"):
            tokens = chat_record.strip().split(",")
            chat_time = tokens[0].strip()
            index = from_timestamp_to_index(chat_time,self.base_time)
            chat_content = tokens[1].strip()
            result = self.tries.search_line(chat_content)
            if len(result) == 0:                continue

            contain_new_word = False
            for word in result:
                if word in key_set:             continue
                self.put_to_dict(word,index)
                key_set.add(word)
                contain_new_word = True

            # do not add a document for the same index
            if contain_new_word and previous_index != index:
                if index not in self.freq_dict:
                    self.freq_dict[index] = 1
                else:
                    self.freq_dict[index] += 1
            previous_index = index

    def put_to_dict(self,word,index):
        if word not in self.word_dict:
            self.word_dict[word] = {}

        if index not in self.word_dict[word]:
            self.word_dict[word][index] = 1
        else:
            self.word_dict[word][index] += 1

    def write_dict_to_db(self):
        conn = sqlite3.connect('testdata/application/time_series/time.db')
        conn.text_factory = str
        date = self.base_time[:10]
        for key in self.word_dict:
            conn.execute('insert into word_freq values(?,?,?)',(key,date,str(self.word_dict[key])))
        conn.commit()
        conn.close()


# from_str_to_timestamp('2013-10-10 23:40:00')
# print from_timestamp_to_index('2013-10-10 00:15:01','2013-10-10 00:00:00')

freq = CountFreq("testdata/application/time_series/key_word", \
                 "testdata/application/time_series/daily",\
                 "2014-07-01 00:00:00")
dict = freq.word_dict
for key in dict:
    print key,dict[key]

dict = freq.freq_dict
for key in dict:
    print key,dict[key]

conn = sqlite3.connect('testdata/application/time_series/time.db')
cursor = conn.execute("select * from word_freq")
for row in cursor:
    print row[0]
