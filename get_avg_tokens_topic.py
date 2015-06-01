#!/usr/bin/python
# coding=utf-8

from argparse import ArgumentParser

parser = ArgumentParser(description="Get the average tokens that belongs to the most frequent topic for health related messages.")
parser.add_argument("-i", "--input_file", type=str, help="input file")

options = parser.parse_args()
input_file = options.input_file

num_tokens = 0
i = 0
for line in open(input_file, 'r'):
    words_list = line.split()[1:]
    max_count = 0
    topic_count = {}

    for word in words_list:
        topic_num = int(word.split(':')[1])
        if topic_num not in topic_count:
            topic_count[topic_num] = 1
        else:
            topic_count[topic_num] += 1
        if topic_count[topic_num] > max_count:
            max_count = topic_count[topic_num]

    num_tokens += max_count
    i += 1

print 'Average tokoens: ' + str(num_tokens * 1.0 / i) 
