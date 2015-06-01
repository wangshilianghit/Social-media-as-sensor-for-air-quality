#!/usr/bin/python
# coding=utf-8

from argparse import ArgumentParser

parser = ArgumentParser(description="get repost health messages from processed health messages.")
parser.add_argument("-i", "--input_file", type=str, help="input processed health messages")
parser.add_argument("-r", "--repost_output", type=str, help="output processed health messages")
parser.add_argument("-o", "--other_output", type=str, help="output processed health messages")

options = parser.parse_args()
input_file = options.input_file
repost_output = options.repost_output
other_output = options.other_output

repost_handle = open(repost_output, 'w')
other_handle = open(other_output, 'w')

i = 0
temp_line = ""
for line in open(input_file, 'r'):
    i += 1
    if i % 2 == 1:
        temp_line = line 
        continue

    index = line.find('http:')
    if index >= 0 and line[index-1] != ':':
        repost_handle.write(temp_line) 
        repost_handle.write(line)
    else:
        other_handle.write(temp_line) 
        other_handle.write(line)



         
