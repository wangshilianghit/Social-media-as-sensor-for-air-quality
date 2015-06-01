#!/usr/bin/python
# coding=utf-8

from sklearn.linear_model import LogisticRegression
from ProduceFeature import ProduceFeature

class LogisticModel:

    def __init__(self):
        self.model = LogisticRegression()
        self.p = None

    def train(self, train_file, label_file, method, n, threshold, question_num, question_type='normal'):
        self.p = ProduceFeature(train_file, label_file)
        training_x = self.p.getX(method, n, threshold, question_type)
        training_y = self.p.getY(question_type)
        self.model.fit(training_x[question_num], training_y[question_num]) 

    def testString(self, s):
        if self.p == None:
            print 'You should train the model before testing'
            exit
        StrX = self.p.getStringX(s)
        return self.model.predict(StrX)
        
    def testFile(self, train_file):
        pass

