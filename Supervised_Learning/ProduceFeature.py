#!/usr/bin/python
# coding=utf-8

class ProduceFeature:
   
    def __init__(self, input_file, label_file, num_questions=6):
        self.input_file = input_file
        self.label_file = label_file
        self.X = [[] for _ in range(num_questions)]
        self.Y = [[] for _ in range(num_questions)]
        self.question_message = [[] for _ in range(num_questions)]
        self.messages = []                     # This is used for storing all messages 
        self.dictionary = {}                   # This dictionary stores any words in the dataset, and the correponding occruances.
        self.word_index = {}
        self.method = None
        self.n = None
        self.num_messages = 0
        self.num_features = 0
        self.num_questions = num_questions

    def __createNgramDict(self, n):
        input_handle = open(self.input_file, 'r')

        for line in input_handle:
            self.messages.append(line)
            words = line.split(' ')
            for i in range(len(words)):
                word = words[i].rstrip()
                if word not in self.dictionary:
                    self.dictionary[word] = 1
                else:
                    self.dictionary[word] += 1
                if n >= 2 and i >= 1:
                    word = words[i-1].rstrip() + "_" + words[i].rstrip()
                    if word not in self.dictionary:
                        self.dictionary[word] = 1
                    else:
                        self.dictionary[word] += 1
                if n >= 3 and i >= 2:
                    word = words[i-2].rstrip() + "_" + words[i-1].rstrip() + "_" + words[i].rstrip()
                    if word not in self.dictionary:
                        self.dictionary[word] = 1
                    else:
                        self.dictionary[word] += 1

        self.num_features = len(self.dictionary)
        self.num_messages = len(self.messages) 

    def __applyTreshold(self, threshold):
        for word in sorted(self.dictionary, key=self.dictionary.get, reverse=True):
            if self.dictionary[word] < threshold:
                self.dictionary.pop(word, None)

        self.num_features = len(self.dictionary) 

    def __getQuestionMessage(self):
        label_handle = open(self.label_file, 'r')
        i = 0
        for line in label_handle:
            cols = line.split()
            for j in range(len(cols)):
                self.question_message[j].append(i)
            i += 1

        label_handle.close()
            
    def __ngramFeature(self, n, threshold, question_type):
        self.__createNgramDict(n)
        self.__applyTreshold(threshold)
        self.__getQuestionMessage()

        i = 0
        for word in sorted(self.dictionary, key=self.dictionary.get, reverse=True):
            self.word_index[word] = i 
            i += 1

        total_x = [[0] * self.num_features for _ in range(self.num_messages)]
        for i in range(len(self.messages)):
            words = self.messages[i].split(' ')
            for j in range(len(words)):
                word = words[j].rstrip()
                if word in self.word_index:
                    total_x[i][self.word_index[word]] = 1
                if n >= 2 and j >= 1:
                    cur_feature = words[j-1].rstrip() + "_" + word
                    if cur_feature in self.word_index:
                        total_x[i][self.word_index[cur_feature]] = 1
                if n >= 3 and j >= 2:
                    cur_feature = words[j-2].rstrip() + "_" + words[j-1].rstrip() + "_" + word
                    if cur_feature in self.word_index:
                        total_x[i][self.word_index[cur_feature]] = 1

        if question_type == 'normal':
            for i in range(0, 6):
                self.X[i] = list(total_x)
        else:
            for i in range(0, 6):
                for index in self.question_message[i]:
                    self.X[i].append(total_x[index])

    def getX(self, method, n, threshold, question_type='normal'):
        self.method = method
        self.n = n
        if method == 'ngram':
            self.__ngramFeature(n, threshold, question_type) 
        return self.X

    def getY(self, question_type='normal'):
        label_handle = open(self.label_file, 'r')
        for line in label_handle:
            cols = line.split()
            i = 0
            for j in range(len(cols)):
                self.Y[j].append(int(cols[j].rstrip()))
                i += 1
            if question_type == 'normal':
                for k in range(i + 1, self.num_questions):
                    self.Y[k].append(0)

        label_handle.close()
        return self.Y

    def __ngramStrFeature(self, s):
        strX = [0] * self.num_features
        words = s.split(' ')        
        for i in range(len(words)):
            word = words[i].rstrip()
            if word in self.word_index:
                strX[self.word_index[word]] = 1
            if self.n >= 2 and i >= 1:
                cur_feature = words[i-1].rstrip() + "_" + word
                if cur_feature in self.word_index:
                    strX[self.word_index[cur_feature]] = 1
            if self.n >= 3 and i >= 2:
                cur_feature = words[i-2].rstrip() + "_" + words[i-1].rstrip() + "_" + word
                if cur_feature in self.word_index:
                    strX[self.word_index[cur_feature]] = 1
        return strX


    def getStringX(self, s):
        if self.method == 'ngram':
            return self.__ngramStrFeature(s)


