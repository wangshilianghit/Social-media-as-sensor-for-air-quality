#!/usr/bin/python
# coding=utf-8

from argparse import ArgumentParser
import ujson as json
import gzip
import sys
import mmseg

parser = ArgumentParser(description="Count the number of Weibo messages for each year, and the number of Weibo users.")
parser.add_argument("-i", "--input_file", nargs='*', help="gz files to be processed")
options = parser.parse_args()
input_list = options.input_file

year_count = {}
user = set()
for input_file in input_list:
    try:
        print 'Processing file: ' + input_file
        file_handle = gzip.open(input_file, 'r')

        for line in file_handle:
            json_weibo = json.loads(line)
            usr_id = json_weibo['usr_id']
            time = json_weibo['created_at']
            year = str(time.split()[5])
            if year not in year_count:
                year_count[year] = 1
            else:
                year_count[year] += 1
            if usr_id not in user:
                user.add(usr_id) 

        print year_count
        print len(user)

    except Exception, e:
        print 'Error in processing file ' + input_file
        print e
        continue

print year_count
print len(user)
