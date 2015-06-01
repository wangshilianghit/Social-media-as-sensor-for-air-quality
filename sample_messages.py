#!/usr/bin/python
# coding=utf-8

from argparse import ArgumentParser

parser = ArgumentParser(description="Get the sample messages for annotation.")
parser.add_argument("-a", "--assign_file", type=str, help="assign file to be processed")
parser.add_argument("-l", "--lda_file", type=str, help="lda file")
parser.add_argument("-t", "--time_file", type=str, help="time file")

options = parser.parse_args()
assign_file = options.assign_file
lda_file = options.lda_file
time_file = options.time_file

id_set = list(line.strip().split()[0] for line in open(lda_file, 'r'))

i = 0
weibo_geo = {}
weibo_content = {}
for line in open(time_file, 'r'):
    i += 1
    if i % 2 == 0:
        weibo_content[weibo_id] = line
        continue
    weibo_id = line.split()[0]
    province = line.split()[7]
    city = line.split()[8]
    verified_type = line.split()[9]
    geo = str(province) + ':' + str(city) + ':' + str(verified_type)
    weibo_geo[weibo_id] = geo 

topics = [97]
categories = [-1]

for topic in topics:
    for category in categories:
        print 'Topic: ' + str(topic)
        print 'Category: ' + str(category)
        geo_count = {}
        geo_topic_count = {}
        i = 0
        for line in open(assign_file, 'r'):
            weibo_id = id_set[i] 
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
            words_list = line.split()[1:]
            number = len(words_list)
            topic_number = 0
            if number == 0:
                i += 1
                continue

            for word in words_list:
                if int(word.split(':')[1]) == topic:
                    topic_number += 1

            if topic_number * 1.0 / number > 0.1:
                print weibo_content[weibo_id] 
            i += 1


