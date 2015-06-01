#!/usr/bin/python

import csv
from argparse import ArgumentParser

def main():
    parser = ArgumentParser(description="Read from .csv file")
    parser.add_argument("-i", "--input_file", type=str, help="The key words file to be processed")
    options = parser.parse_args()

    input_file = options.input_file
    lists = []

    if input_file == None:
        parser.print_help()
        exit(1)

    with open(input_file, 'rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            if row[0].split(',')[2:] in lists:
                print row[0]
                continue
            lists.append(row[0].split(',')[2:])
    
    print lists
    print len(lists)

if __name__ == "__main__":

    main()
