#!/usr/bin/python
# coding=utf-8

from argparse import ArgumentParser

parser = ArgumentParser(description="Preprocessing the text.")
parser.add_argument("-i", "--input_file", type=str, help="input files to be processed")
parser.add_argument("-o", "--output_file", type=str, help="output file")

options = parser.parse_args()
input_file = options.input_file
output_file = options.output_file

input_handle = open(input_file, 'r')
output_handle = open(output_file, 'w')

for line in input_handle:
    words = line.split(' ')
    first = True
    for word in words:
        word = word.rstrip()
        if first == False:
            output_handle.write(' ')
        if word == 'a':
            output_handle.write('1')
        elif word == 'b':
            output_handle.write('0')
        first = False 
    output_handle.write('\n')
