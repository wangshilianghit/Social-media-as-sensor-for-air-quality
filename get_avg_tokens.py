#!/usr/bin/python
# coding=utf-8

from argparse import ArgumentParser

parser = ArgumentParser(description="Get the average tokens for health related messages.")
parser.add_argument("-i", "--input_file", type=str, help="input file")

options = parser.parse_args()
input_file = options.input_file

num_tokens = 0
i = 0
for line in open(input_file, 'r'):
    words_list = line.split()[1:]
    num_tokens += len(words_list)
    i += 1

print 'Average tokoens: ' + str(num_tokens * 1.0 / i) 
