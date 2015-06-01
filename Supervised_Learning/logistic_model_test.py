#!/usr/bin/python
# coding=utf-8

import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import cross_val_score
from argparse import ArgumentParser
from ProduceFeature import ProduceFeature 
from sklearn.metrics import precision_score, make_scorer, recall_score, f1_score

parser = ArgumentParser(description="Preprocessing the text.")
parser.add_argument("-i", "--input_file", type=str, help="Input file for training the model")
parser.add_argument("-l", "--label_file", type=str, help="Label for traning file")
parser.add_argument("-c", "--cv_num", type=int, default=10, help="The number of passes for cross validation")

options = parser.parse_args()
input_file = options.input_file
label_file = options.label_file
cv_num = options.cv_num


for n in range(1, 4):
    for threshold in range (1, 4):
        print 'ngram: n='+ str(n)
        print 'Threshold: ' + str(threshold)
        p = ProduceFeature(input_file, label_file)
        training_x = p.getX('ngram', n, threshold)
        training_y = p.getY()

        model = LogisticRegression()
        score_accuracy = [0] * 6
        score_precision = [0] * 6
        score_recall = [0] * 6
        score_f1 = [0] * 6
        questions = [0, 2]
        for i in questions:
            score_accuracy[i] = cross_val_score(model, training_x[i], training_y[i], scoring='accuracy', cv=cv_num)
            score_precision[i] = cross_val_score(model, training_x[i], training_y[i], scoring=make_scorer(precision_score, average='micro'), cv=cv_num)
            score_recall[i] = cross_val_score(model, training_x[i], training_y[i], scoring=make_scorer(recall_score, average='micro'), cv=cv_num)
            score_f1[i] = cross_val_score(model, training_x[i], training_y[i], scoring=make_scorer(f1_score, average='micro'), cv=cv_num)
            print 'Question ' + str(i + 1) + ': Accuray: ' + str(score_accuracy[i].mean()) + '  Precision: ' + str(score_precision[i].mean()) \
            + '  Recall: ' + str(score_recall[i].mean()) + '  F1: ' + str(score_f1[i].mean())
            print 

