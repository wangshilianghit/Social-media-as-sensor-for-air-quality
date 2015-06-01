#!/usr/bin/python
# coding=utf-8

from argparse import ArgumentParser
import ujson as json
import gzip
import sys
import mmseg

parser = ArgumentParser(description="Load .gz files")
parser.add_argument("-i", "--input_file", nargs='*', help="gz files to be processed")
parser.add_argument("-k", "--keyword_file", type=str, help="keyword file")
parser.add_argument("-o", "--output_file", type=str, help="result file")
parser.add_argument("-j", "--output_json", type=str, help="result file")

options = parser.parse_args()
input_list = options.input_file
keyword_file = options.keyword_file
output_file = options.output_file
#output_json = options.output_json

total_weibos = 0
total_disease_weibos = 0

output_handle = open(output_file, 'w')
#output_json = open(output_json, 'w')

for input_file in input_list:
    try:
        print 'Processing file: ' + input_file
        #output_handle.write('Processing file: ' + input_file + '\n');
        file_handle = gzip.open(input_file, 'r')

        mmseg.mmseg.dict_load_defaults()

        # Read the key words from the file
        keyword_set = set(line.strip() for line in open(keyword_file, 'r'))

        for line in file_handle:
            total_weibos = total_weibos + 1
            json_weibo = json.loads(line)
            weibo_id = json_weibo['id']
            created_at = json_weibo['created_at']
            created_at = created_at.encode('utf-8')
            province = json_weibo['user']['province']
            province = province.encode('utf-8')
            city = json_weibo['user']['city']
            city = city.encode('utf-8')
            verified_type = json_weibo['user']['verified_type']
            user_id = json_weibo['user']['id']
            text = json_weibo['text']
            text = text.encode('utf-8')
            if text.find('//') >= 0:
                text = text[ : text.find('//')]
                
            tokens = mmseg.mmseg.Algorithm(text)
            exist = False
            exist_key = []
            for token in tokens:
                if str(token) in keyword_set:
                    total_disease_weibos = total_disease_weibos + 1
                    exist_key.append(str(token))
                    exist = True
            if exist == True:
                output_handle.write(str(weibo_id))
                output_handle.write(' ' + created_at + ' ' + province + ' ' + city + ' ' + str(verified_type) + ' ' + str(user_id) + '\n')
                output_handle.write(text + '\n')
                '''
                json.dump(json_weibo, output_json)
                output_json.write('\n')
                '''
                print_key = ''
                for key in exist_key:
                    print_key = print_key + key + ' '
                #output_handle.write('Key: ' + print_key + '\n')

        print 'Total Weibos so far: ' + str(total_weibos)
        print 'Total disease related Weibos so far: ' + str(total_disease_weibos)
        #output_handle.write('Total Weibos so far: ' + str(total_weibos))
        #output_handle.write('Total disease related Weibos so far: ' + str(total_disease_weibos))
        #output_handle.write('\n\n');

    except Exception, e:
        print 'Error in processing file ' + input_file
        print e
        #output_handle.write('Error in processing file ' + input_file)
        continue

print 'Total Weibos: ' + str(total_weibos)
print 'Total disease related Weibos: ' + str(total_disease_weibos)
#output_handle.write('Total Weibos: ' + str(total_weibos))
#output_handle.write('Total disease related Weibos: ' + str(total_disease_weibos))


