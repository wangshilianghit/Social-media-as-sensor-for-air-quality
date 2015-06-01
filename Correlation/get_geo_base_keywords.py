#!/usr/bin/python
# coding=utf-8

from argparse import ArgumentParser
import ujson as json
import gzip
import sys
import mmseg

parser = ArgumentParser(description="get the baseline for geo pollution")
parser.add_argument("-i", "--input_file", type=str, help="input processed health related weibo files")
parser.add_argument("-k", "--keyword_file", type=str, help="keywords for processing")
options = parser.parse_args()
input_file = options.input_file
keyword_file = options.keyword_file

categories = [-1, 1, 2, 3, 10]

weibos = []
attributes = []

i = 0
for line in open(input_file, 'r'):
    i += 1
    if i % 2 == 0:
        weibos.append(line)
    else:
        attributes.append(line)
        
keyword_set = set(line.strip() for line in open(keyword_file, 'r'))

for category in categories:
    print 'Category: ' + str(category)
    geo_count = {}
    geo_topic_count = {}
    i = 0
    for line in attributes:
        weibo_id = line.split()[0]
        province = line.split()[7]
        city = line.split()[8]
        verified_type = line.split()[9]
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

        text = weibos[i]
        tokens = mmseg.mmseg.Algorithm(text)
        for token in tokens:
            if str(token) in keyword_set:
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



