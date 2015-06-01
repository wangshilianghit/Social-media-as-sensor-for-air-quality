#!/usr/bin/python
# coding=utf-8

from argparse import ArgumentParser
import mmseg

parser = ArgumentParser(description="Preprocessing the text.")
parser.add_argument("-i", "--input_file", type=str, help="input files to be processed")
parser.add_argument("-o", "--output_file", type=str, help="output file")

options = parser.parse_args()
input_file = options.input_file
output_file = options.output_file
general_file = "general_words.txt"
stop_file = "stopwords.txt"

input_handle = open(input_file, 'r')
output_handle = open(output_file, 'w')

general_set = set(line.strip() for line in open(general_file, 'r'))
stop_set = set(line.strip() for line in open(stop_file, 'r'))

PUNCTUATION = ('，', '！', '“', '？', '。', '【', '】', '●', '（', '）', '、', 'http')

mmseg.mmseg.dict_load_defaults()

i = 0
dictionary = set()

for line in input_handle:
    i += 1
    if i % 2 == 1:
        weibo_id = line.strip() 
    else:
        tokens = mmseg.mmseg.Algorithm(line)
        first = True
        for token in tokens:
            if str(token) in PUNCTUATION:
                continue
            if str(token) not in general_set:
                continue
            if str(token) in stop_set:
                continue
            if first == True: 
                output_handle.write(str(token))
            else:
                output_handle.write(' ' + str(token))
            first = False
        output_handle.write('\n')

