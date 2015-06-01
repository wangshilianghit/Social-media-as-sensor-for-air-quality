#!/usr/bin/python
# coding=utf-8

d = {}
d['apple'] = 1
d['big'] = 3
d['cat'] = 2
for w in sorted(d, key=d.get, reverse=True):
    print w, d[w]
