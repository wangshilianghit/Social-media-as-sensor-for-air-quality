#!/usr/bin/python
# coding=utf-8

from argparse import ArgumentParser

parser = ArgumentParser(description="count the number of messages each month for given topics")
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
weibo_userid = {}

for line in open(time_file, 'r'):
    i += 1
    if i % 2 == 0:
        continue
    weibo_id = line.split()[0]
    province = line.split()[7]
    city = line.split()[8]
    verified_type = line.split()[9]
    user_id = line.split()[10]
    geo = str(province) + ':' + str(city) + ':' + str(verified_type)
    weibo_geo[weibo_id] = geo 
    weibo_userid[weibo_id] = user_id

count_weibo = {}
count_weibo['0'] = 0
count_weibo['1'] = 0
count_weibo['2'] = 0
count_weibo['3'] = 0
count_user = {}
count_user['0'] = {}
count_user['1'] = {}
count_user['2'] = {}
count_user['3'] = {}
count_total_user = {}

i = 0
for line in open(assign_file, 'r'):
    weibo_id = id_set[i] 
    if weibo_id not in weibo_geo:
        i += 1
        continue
    geo = weibo_geo[weibo_id]
    verified_type = geo.split(':')[2]
    user_id = weibo_userid[weibo_id]

    if int(verified_type) in [-1, 0, 200, 220, 400]:
        count_weibo['0'] += 1
        count_user['0'].setdefault(user_id, 1) 
        count_total_user.setdefault(user_id, 1)
    elif verified_type == '1':
        count_weibo['1'] += 1
        count_user['1'].setdefault(user_id, 1) 
        count_total_user.setdefault(user_id, 1)
    elif verified_type == '2':
        count_weibo['2'] += 1
        count_user['2'].setdefault(user_id, 1) 
        count_total_user.setdefault(user_id, 1)
    elif verified_type == '3':
        count_weibo['3'] += 1
        count_user['3'].setdefault(user_id, 1) 
        count_total_user.setdefault(user_id, 1)
    i += 1


print 'The number of weibos for each user class'
print 'class 0: ' + str(count_weibo['0'])
print 'class 1: ' + str(count_weibo['1'])
print 'class 2: ' + str(count_weibo['2'])
print 'class 3: ' + str(count_weibo['3'])

print 'The number of users for each user class'
print 'class 0: ' + str(len(count_user['0']))
print 'class 1: ' + str(len(count_user['1']))
print 'class 2: ' + str(len(count_user['2']))
print 'class 3: ' + str(len(count_user['3']))

print 'The number of users for all user class: ' + str(len(count_total_user))
