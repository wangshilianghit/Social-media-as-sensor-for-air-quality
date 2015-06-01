#!/usr/bin/python
# coding=utf-8

from argparse import ArgumentParser

parser = ArgumentParser(description="count the number of messages each month for given topics")
parser.add_argument("-a", "--assign_file", type=str, help="assign file to be processed")
parser.add_argument("-l", "--lda_file", type=str, help="lda file")
parser.add_argument("-t", "--time_file", type=str, help="time file")

options = parser.parse_args()
assign_file = options.assign_file
lda_file = options.lda_file
time_file = options.time_file

id_set = list(line.strip().split()[0] for line in open(lda_file, 'r'))

topics = [97, 69]

for topic in topics:
    print 'Topic: ' + str(topic)
    i = 0
    number = 0
    for line in open(assign_file, 'r'):
        weibo_id = id_set[i] 
        words_list = line.split()[1:]
        for word in words_list:
            if int(word.split(':')[1]) == topic:
                number += 1
                break
        i += 1
    print 'Number: ' + str(number) 


