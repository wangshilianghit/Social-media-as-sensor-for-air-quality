#!/usr/bin/python
# coding=utf-8

import numpy as np
from sklearn import svm
from sklearn.cross_validation import cross_val_score
from argparse import ArgumentParser
from ProduceFeature import ProduceFeature

parser = ArgumentParser(description="Preprocessing the text.")
parser.add_argument("-i", "--input_file", type=str, help="Input file for training the model")
parser.add_argument("-l", "--label_file", type=str, help="Label for traning file")
parser.add_argument("-n", "--training_num", type=int, default=170, help="The number of messages for training")
parser.add_argument("-c", "--cv_num", type=int, default=10, help="The number of passes for cross validation")
parser.add_argument("-C", "--C_value", type=int, default=0.1, help="The value of parameter C")
parser.add_argument("-k", "--kernel", type=str, default='linear', help="Kernel used for SVM model")

options = parser.parse_args()
input_file = options.input_file
label_file = options.label_file
training_num = options.training_num
cv_num = options.cv_num
C_value = options.C_value
kernel = options.kernel

p = ProduceFeature(input_file, label_file, training_num)
training_x = p.getX('keywords', 2)
training_y = p.getY()

model = svm.SVC(kernel=kernel, C=C_value)
score_accuracy = [0] * 6
for i in range (0, 6):
    score_accuracy[i] = cross_val_score(model, training_x[i], training_y[i], scoring='accuracy', cv=cv_num)
    print 'Question ' + str(i + 1) + '\'s accuracy: ' + str(score_accuracy[i].mean())

