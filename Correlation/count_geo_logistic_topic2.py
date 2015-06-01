#!/usr/bin/python
# coding=utf-8

import sys
sys.path.insert(0, '/home/swang/Research/program/Supervised_Learning')
from argparse import ArgumentParser
from LogisticModel import LogisticModel

parser = ArgumentParser(description="count the number of messages for every cities that returns true for the result of the logistic model, and belongs to topic 97.")
parser.add_argument("-i", "--input_file", type=str, help="Input file for processing")
parser.add_argument("-m", "--message_info", type=str, help="File that stores weibo messages info")
parser.add_argument("-a", "--assign_file", type=str, help="File that assigns topics for each words.")
parser.add_argument("-t", "--train_file", type=str, help="The training file for Logistic Model") 
parser.add_argument("-l", "--label_file", type=str, help="The label for traing file ") 

options = parser.parse_args()
input_file = options.input_file
message_info = options.message_info
assign_file = options.assign_file
train_file = options.train_file
label_file = options.label_file

i = 0
weibo_geo = {}
for line in open(message_info, 'r'):
    i += 1
    if i % 2 == 0:
        continue
    weibo_id = line.split()[0]
    province = line.split()[7]
    city = line.split()[8]
    verified_type = line.split()[9]
    geo = str(province) + ':' + str(city) + ':' + str(verified_type)
    weibo_geo[weibo_id] = geo 

# Train the Logistic Model
method = 'ngram'
ns = [1, 2, 3]
thresholds = [1, 2, 3]
question = 3

for n in ns:
    for threshold in thresholds:

        # We just use the best model for qestion 1
        model_q1 = LogisticModel()
        model_q1.train(train_file, label_file, method, 3, 1, 0)

        # The classifier for question 3 would be trained on the subset of 114 messages.
        model_q3 = LogisticModel()
        model_q3.train(train_file, label_file, method, n, threshold, 2, 'unnormal')
        print 'Training method: ' + method
        print 'Feature number: ' + str(n)
        print 'threshold: ' + str(threshold)
        print 'Question: ' + str(question)

        id_list = []
        model_result_q1 = []
        model_result_q3 = []
        for line in open(input_file, 'r'):
            id_list.append(line.split()[0])
            index = line.find(' ') + 1
            messageStr = line[index:]
            results = model_q1.testString(messageStr)
            model_result_q1.append(results[0])

            results = model_q3.testString(messageStr)
            model_result_q3.append(results[0])

        topic = 97
        category = 10 

        print 'Topic: ' + str(topic)
        print 'Category: ' + str(category)
        geo_count = {}
        geo_topic_count = {}
        i = 0
        for line in open(assign_file, 'r'):
            weibo_id = id_list[i] 
            if weibo_id not in weibo_geo:
                i += 1
                continue
            geo = weibo_geo[weibo_id]
            province = geo.split(':')[0]
            city = geo.split(':')[1]
            verified_type = geo.split(':')[2]
            geo = province + ':' + city 

            if category == -1:
                if int(verified_type) not in [-1, 0, 200, 220, 400]:
                    i += 1
                    continue
            elif category == 10:
                pass
            else:
                if int(verified_type) != category:
                    i += 1
                    continue

            if geo not in geo_count:
                geo_count[geo] = 1
            else:
                geo_count[geo] += 1

            if int(model_result_q1[i]) == 0 or int(model_result_q3[i]) == 0:
                i += 1
                continue

            words_list = line.split()[1:]
            for word in words_list:
                if int(word.split(':')[1]) == topic:
                    if geo not in geo_topic_count:
                        geo_topic_count[geo] = 1
                    else:
                        geo_topic_count[geo] += 1
                    break
            i += 1

        geo_normalized_count = dict((key, geo_topic_count[key] * 1.0 / geo_count[key]) for key, value in geo_topic_count.items())

        locations = [['13', '5'], ['13', '1'], ['13', '6'], ['13', '4'], ['13', '11'], ['13', '2'], ['37', '1'], ['13', '10'], ['61', '1'], ['41', '1'], ['12', '1'], ['13', '9'], ['11', '1'], ['42', '1'], ['51', '1'], ['65', '1'], ['34', '1'], ['32', '12'], ['32', '8'], ['43', '1'], ['32', '2'], ['23', '1'], ['32', '4'], ['32', '1'], ['32', '3'], ['14', '1'], ['33', '5'], ['21', '1'], ['32', '11'], ['32', '10'], ['32', '13'], ['32', '6'], ['22', '1'], ['36', '1'], ['33', '7'], ['32', '7'], ['62', '1'], ['32', '5'], ['32', '9'], ['33', '4'], ['33', '8'], ['33', '6'], ['33', '1'], ['13', '3'], ['50', '1'], ['63', '1'], ['37', '2'], ['31', '1'], ['15', '1'], ['33', '3'], ['44', '2'], ['45', '1'], ['33', '10'], ['44', '6'], ['44', '1'], ['13', '8'], ['21', '2'], ['33', '2'], ['52', '1'], ['44', '7'], ['33', '11'], ['44', '20'], ['44', '19'], ['64', '1'], ['13', '7'], ['44', '3'], ['44', '4'], ['44', '13'], ['53', '1'], ['35', '1'], ['33', '9'], ['35', '2'], ['54', '1'], ['46', '1']]

        print 'Normalized'
        for location in locations:
            key = location[0] + ':' + location[1] 
            if key in geo_normalized_count:
                print str(format(geo_normalized_count[key], '.4g'))
            else:
                print 0.0000

        print 'Topic related Weibos'
        for location in locations:
            key = location[0] + ':' + location[1] 
            if key in geo_topic_count:
                print geo_topic_count[key] 
            else:
                print 0

        print 'Total Weibos'
        for location in locations:
            key = location[0] + ':' + location[1] 
            if key in geo_count:
                print geo_count[key] 
            else:
                print 0

