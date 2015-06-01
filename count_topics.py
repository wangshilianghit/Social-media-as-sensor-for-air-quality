#!/usr/bin/python
# coding=utf-8

from argparse import ArgumentParser

parser = ArgumentParser(description="count the nunber of messages each month for given topics")
parser.add_argument("-a", "--assign_file", type=str, help="assign file to be processed")
parser.add_argument("-l", "--lda_file", type=str, help="lda file")
parser.add_argument("-t", "--time_file", type=str, help="time file")

options = parser.parse_args()
assign_file = options.assign_file
lda_file = options.lda_file
time_file = options.time_file

id_set = list(line.strip().split()[0] for line in open(lda_file, 'r'))

i = 0
weibo_time = {}
for line in open(time_file, 'r'):
    i += 1
    if i % 2 == 0:
        continue
    weibo_id = line.split()[0]
    month = line.split()[2]
    year = line.split()[6]
    date = str(year) + ':' + str(month)
    weibo_time[weibo_id] = date

topics = [2, 95, 37, 90]

for topic in topics:
    print topic
    month_count = {}
    month_topic_count = {}
    i = 0
    for line in open(assign_file, 'r'):
        weibo_id = id_set[i] 
        if weibo_id in weibo_time:
            date = weibo_time[weibo_id]
            month = date.split(':')[1]
            year = date.split(':')[0]
            if date not in month_count:
                month_count[date] = 1
            else:
                month_count[date] += 1
        words_list = line.split()[1:]

        for word in words_list:
            if int(word.split(':')[1]) == topic:
                if date not in month_topic_count:
                    month_topic_count[date] = 1
                else:
                    month_topic_count[date] += 1
                break
        i += 1

    month_normalized_count = dict((key, month_topic_count[key] * 1.0 / month_count[key]) for key, value in month_topic_count.items())

    weeks = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    years = ['2012','2013']

    for year in years:
        for week in weeks:
            key = year + ':' + week
            print str(format(month_normalized_count[key], '.4g'))

