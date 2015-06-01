#!/usr/bin/python
# coding=utf-8

from argparse import ArgumentParser

parser = ArgumentParser(description="count the nunber of health related messages for each year")
parser.add_argument("-i", "--input_file", type=str, help="input file")

options = parser.parse_args()
input_file = options.input_file

i = 0
year_count = {}
for line in open(input_file, 'r'):
    i += 1
    if i % 2 == 0:
        continue
    year = str(line.split()[6])
    if year not in year_count:
        year_count[year] = 1
    else:
        year_count[year] += 1

print year_count
