#!/usr/bin/python
# coding=utf-8

import sys
sys.path.insert(0, '/home/swang/Research/program/Supervised_Learning')
from argparse import ArgumentParser
from LogisticModel import LogisticModel

parser = ArgumentParser(description="count the number of messages each month for given topics")
parser.add_argument("-i", "--input_file", type=str, help="Input file for processing")
parser.add_argument("-m", "--message_info", type=str, help="File that stores weibo messages info")
parser.add_argument("-t", "--train_file", type=str, help="The training file for Logistic Model") 
parser.add_argument("-l", "--label_file", type=str, help="The label for traing file ") 
options = parser.parse_args()
input_file = options.input_file
message_info = options.message_info
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
n = 3
threshold = 1
question = 3
model = LogisticModel()
model.train(train_file, label_file, method, n, threshold, question-1)
print 'Training method: ' + method
print 'Feature number: ' + str(n)
print 'threshold: ' + str(threshold)
print 'Question: ' + str(question)

categories = [10]

for category in categories:
    print 'Category: ' + str(category)
    geo_count = {}
    geo_topic_count = {}
    for line in open(input_file, 'r'):
        weibo_id = line.split()[0] 
        if weibo_id not in weibo_geo:
            continue
        geo = weibo_geo[weibo_id]
        province = geo.split(':')[0]
        city = geo.split(':')[1]
        verified_type = geo.split(':')[2]
        geo = province + ':' + city 

        if category == -1:
            if int(verified_type) not in [-1, 0, 200, 220, 400]:
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

        index = line.find(' ') + 1
        messageStr = line[index:]
        results = model.testString(messageStr)
        if int(results[0]) == 1:
            if geo not in geo_topic_count:
                geo_topic_count[geo] = 1
            else:
                geo_topic_count[geo] += 1

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

