#!/usr/bin/python
# coding=utf-8

from argparse import ArgumentParser
import ujson as json
import gzip
import sys
import mmseg

parser = ArgumentParser(description="get the baseline for geo pollution")
parser.add_argument("-i", "--input_file", type=str, help="input processed health related weibo files")
parser.add_argument("-k", "--keyword_file", type=str, help="keywords for processing")
options = parser.parse_args()
input_file = options.input_file
keyword_file = options.keyword_file

weibos = []
attributes = []

i = 0
for line in open(input_file, 'r'):
    i += 1
    if i % 2 == 0:
        weibos.append(line)
    else:
        attributes.append(line)
        
keyword_set = set(line.strip() for line in open(keyword_file, 'r'))

i = 0
number = 0
for line in attributes:
    text = weibos[i]
    tokens = mmseg.mmseg.Algorithm(text)
    for token in tokens:
        if str(token) in keyword_set:
            number += 1 
            break
    i += 1

print 'Number: ' + str(number) 



