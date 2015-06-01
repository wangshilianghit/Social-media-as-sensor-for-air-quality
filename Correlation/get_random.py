#!/usr/bin/python
# coding=utf-8

import sys
import random

if len(sys.argv) != 4:
    print 'argument not valid'
    sys.exit(-1)

input_file = sys.argv[1]
output_file = sys.argv[2]
max_num = int(sys.argv[3])

text_list = []

input_handle = open(input_file, 'r')
output_handle = open(output_file, 'w')

num_line = 0
for word in input_handle:
    text_list.append(word)
    num_line = num_line + 1

random.seed(0)
number_list = []
i = 0
while i < max_num:
    number = random.randint(0, num_line-1)
    if number not in number_list:
        number_list.append(number)
        i = i + 1

print len(number_list)
for i in number_list:
    output_handle.write(text_list[i])


