#!/usr/bin/python
# coding=utf-8

from argparse import ArgumentParser
import mmseg

parser = ArgumentParser(description="count the number of messages each month for given topics")
parser.add_argument("-a", "--assign_file", type=str, help="assign file to be processed")
parser.add_argument("-l", "--lda_file", type=str, help="lda file")
parser.add_argument("-t", "--time_file", type=str, help="time file")
parser.add_argument("-o", "--output_file", type=str, help="output file")
options = parser.parse_args()
assign_file = options.assign_file
lda_file = options.lda_file
time_file = options.time_file
output_file = options.output_file

id_set = list(line.strip().split()[0] for line in open(lda_file, 'r'))
output = open(output_file, 'w')

i = 0
weibos = []
weibo_geo = {}
for line in open(time_file, 'r'):
    i += 1
    if i % 2 == 0:
        weibos.append(line)
    else:
        weibo_id = line.split()[0]
        province = line.split()[7]
        city = line.split()[8]
        verified_type = line.split()[9]
        geo = str(province) + ':' + str(city) + ':' + str(verified_type)
        weibo_geo[weibo_id] = geo 

keyword_set = set(['空气', '污染'])
topics = [97, 69]
numbers = [0] * 8

i = 0
for line in open(assign_file, 'r'):
    weibo_id = id_set[i] 
    words_list = line.split()[1:]
    tag_list = ['False'] * 8
    text = weibos[i]

    # Filter 1: AQ (Topic 97)
    for word in words_list:
        if int(word.split(':')[1]) == 97:
            tag_list[0] = 'True'
            numbers[0] += 1
            break
    # Filter 2: PO (Topic 69)
    for word in words_list:
        if int(word.split(':')[1]) == 69:
            tag_list[1] = 'True'
            numbers[1] += 1
            break
    # Filter 3: 'air'
    tokens = mmseg.mmseg.Algorithm(text)
    for token in tokens:
        if str(token) == '空气':
            tag_list[2] = 'True'
            numbers[2] += 1
            break
    # Filter 4: 'pollution'
    tokens = mmseg.mmseg.Algorithm(text)
    for token in tokens:
        if str(token) == '污染':
            tag_list[3] = 'True'
            numbers[3] += 1
            break
    # Filter 5: 'breath'
    tokens = mmseg.mmseg.Algorithm(text)
    for token in tokens:
        if str(token) == '呼吸':
            tag_list[4] = 'True'
            numbers[4] += 1
            break
    # Filter 6: 'cough'
    tokens = mmseg.mmseg.Algorithm(text)
    for token in tokens:
        if str(token) == '咳嗽':
            tag_list[5] = 'True'
            numbers[5] += 1
            break
    # Filter 7: AQ + 'air'
    tokens = mmseg.mmseg.Algorithm(text)
    for token in tokens:
        if tag_list[0] == 'True' and tag_list[2] == 'True':
            tag_list[6] = 'True'
            numbers[6] += 1
            break
    # Filter 8: AQ + 'pollution'
    tokens = mmseg.mmseg.Algorithm(text)
    for token in tokens:
        if tag_list[0] == 'True' and tag_list[3] == 'True':
            tag_list[7] = 'True'
            numbers[7] += 1
            break
    i += 1

    output.write(weibo_id + '\t')
    for tag in tag_list:
        output.write(tag + '\t')
    output.write('\n')

for number in numbers:
    print number
