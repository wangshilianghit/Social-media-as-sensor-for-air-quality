#!/usr/bin/python

import sys

if (len(sys.argv)) != 6:
    print 'arg error'
    exit 

input_file = sys.argv[1]
file_name1 = sys.argv[2]
file_name2 = sys.argv[3]
file_name3 = sys.argv[4]
output_file = sys.argv[5]

word_list1 = list(line.strip() for line in open(file_name1, 'r'))
word_list2 = list(line.strip() for line in open(file_name2, 'r'))
word_list3 = list(line.strip() for line in open(file_name3, 'r'))

output_handle = open(output_file, 'w')
for line in open(input_file, 'r'):
    word = line.strip()
    if word in word_list1 and word in word_list2:
        output_handle.write(word + "\t" + "diseases\\symptoms\n")
    elif word in word_list2 and word in word_list3:
        output_handle.write(word + "\t" + "symptoms\\treatments\n")
    elif word in word_list1 and word in word_list3:
        output_handle.write(word + "\t" + "diseases\\treatments\n")
    elif word in word_list1:
        output_handle.write(word + "\t" + "diseases\n")
    elif word in word_list2:
        output_handle.write(word + "\t" + "symptoms\n")
    elif word in word_list3:
        output_handle.write(word + "\t" + "treatments\n")
    else:
        output_handle.write(word + "\t" + "symptoms\n")

