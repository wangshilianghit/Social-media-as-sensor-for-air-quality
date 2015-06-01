#!/usr/bin/python
# coding=utf-8

import numpy as np
from sklearn.cross_validation import cross_val_score
from argparse import ArgumentParser
from LogisticModel import LogisticModel
from sklearn.metrics import precision_score, make_scorer, recall_score, f1_score

parser = ArgumentParser(description="Preprocessing the text.")
parser.add_argument("-i", "--input_file", type=str, help="Input file for training the model")
parser.add_argument("-l", "--label_file", type=str, help="Label for traning file")
parser.add_argument("-t", "--test_file", type=str, help="Input file for testing")

options = parser.parse_args()
input_file = options.input_file
label_file = options.label_file
test_file = options.test_file
test_handle = open(test_file, 'r')

model = LogisticModel()
model.train(input_file, label_file, 'ngram', 1, 2, 2)

for line in test_handle:
    print line
    print model.testString(line)


