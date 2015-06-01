#!/usr/bin/python
# coding=utf-8

import csv

array1 = []
array2 = []

with open('1.csv', 'rb') as csvfile1:
    spamreader = csv.reader(csvfile1, delimiter=',', quotechar='|')
    i = 0
    for row in spamreader:
        if i >= 1 and i <= 170:
            array1.append(row)
        i += 1

with open('2.csv', 'rb') as csvfile2:
    spamreader = csv.reader(csvfile2, delimiter=',', quotechar='|')
    i = 0
    for row in spamreader:
        if i >= 1 and i <= 170:
            array2.append(row)
        i += 1

num1 = 0
num2 = 0
num3 = 0
num4 = 0
num5 = 0
num6 = 0
same_yes1 = 0
same_no1 = 0
a_yes1 = 0
a_no1 = 0
b_yes1 = 0
b_no1 = 0
same_yes2 = 0
same_no2 = 0
a_yes2 = 0
a_no2 = 0
b_yes2 = 0
b_no2 = 0
same_yes3 = 0
same_no3 = 0
a_yes3 = 0
a_no3 = 0
b_yes3 = 0
b_no3 = 0
same_yes4 = 0
same_no4 = 0
a_yes4 = 0
a_no4 = 0
b_yes4 = 0
b_no4 = 0
same_yes5 = 0
same_no5 = 0
a_yes5 = 0
a_no5 = 0
b_yes5 = 0
b_no5 = 0
same_yes6 = 0
same_no6 = 0
a_yes6 = 0
a_no6 = 0
b_yes6 = 0
b_no6 = 0
for row1, row2 in zip(array1, array2):
    num1 += 1
    if row1[1] == 'a' and row2[1] == 'b':
        a_yes1 += 1
        b_no1 += 1
    if row1[1] == 'b' and row2[1] == 'a':
        a_no1 += 1
        b_yes1 += 1
    if row1[1] == row2[1] and row1[1] == 'b':
        same_no1 += 1 
        a_no1 += 1
        b_no1 += 1
    if row1[1] == row2[1] and row1[1] == 'a':
        same_yes1 += 1
        a_yes1 += 1
        b_yes1 += 1
        num2 += 1
        num3 += 1

        if row1[2] == 'a' and row2[2] == 'b':
            a_yes2 += 1
            b_no2 += 1
        if row1[2] == 'b' and row2[2] == 'a':
            a_no2 += 1
            b_yes2 += 1
        if row1[2] == row2[2] and row1[2] == 'b':
            same_no2 += 1 
            a_no2 += 1
            b_no2 += 1
        if row1[2] == row2[2] and row1[2] == 'a':
            same_yes2 += 1
            a_yes2 += 1
            b_yes2 += 1

        if row1[3] == 'a' and row2[3] == 'b':
            a_yes3 += 1
            b_no3 += 1
        if row1[3] == 'b' and row2[3] == 'a':
            a_no3 += 1
            b_yes3 += 1
        if row1[3] == row2[3] and row1[3] == 'b':
            same_no3 += 1 
            a_no3 += 1
            b_no3 += 1
        if row1[3] == row2[3] and row1[3] == 'a':
            same_yes3 += 1
            a_yes3 += 1
            b_yes3 += 1
            num4 += 1
            num5 += 1
            num6 += 1

            if row1[4] == 'a' and row2[4] == 'b':
                a_yes4 += 1
                b_no4 += 1
            if row1[4] == 'b' and row2[4] == 'a':
                a_no4 += 1
                b_yes4 += 1
            if row1[4] == row2[4] and row1[4] == 'b':
                same_no4 += 1 
                a_no4 += 1
                b_no4 += 1
            if row1[4] == row2[4] and row1[4] == 'a':
                same_yes4 += 1
                a_yes4 += 1
                b_yes4 += 1

            if row1[5] == 'a' and row2[5] == 'b':
                a_yes5 += 1
                b_no5 += 1
            if row1[5] == 'b' and row2[5] == 'a':
                a_no5 += 1
                b_yes5 += 1
            if row1[5] == row2[5] and row1[5] == 'b':
                same_no5 += 1 
                a_no5 += 1
                b_no5 += 1
            if row1[5] == row2[5] and row1[5] == 'a':
                same_yes5 += 1
                a_yes5 += 1
                b_yes5 += 1

            if row1[6] == 'a' and row2[6] == 'b':
                a_yes6 += 1
                b_no6 += 1
            if row1[6] == 'b' and row2[6] == 'a':
                a_no6 += 1
                b_yes6 += 1
            if row1[6] == row2[6] and row1[6] == 'b':
                same_no6 += 1 
                a_no6 += 1
                b_no6 += 1
            if row1[6] == row2[6] and row1[6] == 'a':
                same_yes6 += 1
                a_yes6 += 1
                b_yes6 += 1

ob_1 = 1.0 * (same_yes1 + same_no1) / num1 
ob_2 = 1.0 * (same_yes2 + same_no2) / num2 
ob_3 = 1.0 * (same_yes3 + same_no3) / num3 
ob_4 = 1.0 * (same_yes4 + same_no4) / num4 
ob_5 = 1.0 * (same_yes5 + same_no5) / num5 
ob_6 = 1.0 * (same_yes6 + same_no6) / num6 

rand_1 = (1.0 * a_yes1 / num1)  * (1.0 * b_yes1 / num1) + (1.0 * a_no1 / num1) * (1.0 * b_no1 / num1) 
rand_2 = (1.0 * a_yes2 / num2)  * (1.0 * b_yes2 / num2) + (1.0 * a_no2 / num2) * (1.0 * b_no2 / num2) 
rand_3 = (1.0 * a_yes3 / num3)  * (1.0 * b_yes3 / num3) + (1.0 * a_no3 / num3) * (1.0 * b_no3 / num3) 
rand_4 = (1.0 * a_yes4 / num4)  * (1.0 * b_yes4 / num4) + (1.0 * a_no4 / num4) * (1.0 * b_no4 / num4) 
rand_5 = (1.0 * a_yes5 / num5)  * (1.0 * b_yes5 / num5) + (1.0 * a_no5 / num5) * (1.0 * b_no5 / num5) 
rand_6 = (1.0 * a_yes6 / num6)  * (1.0 * b_yes6 / num6) + (1.0 * a_no6 / num6) * (1.0 * b_no6 / num6) 

result_1 = (ob_1 - rand_1) / (1 - rand_1)
result_2 = (ob_2 - rand_2) / (1 - rand_2)
result_3 = (ob_3 - rand_3) / (1 - rand_3)
result_4 = (ob_4 - rand_4) / (1 - rand_4)
result_5 = (ob_5 - rand_5) / (1 - rand_5)
result_6 = (ob_6 - rand_6) / (1 - rand_6)

print 'Observed agreement1: ' + str(ob_1)
print 'same_yes: ' + str(same_yes1)
print 'same_no: ' + str(same_no1)
print 'num: ' + str(num1)
print 'Observed agreement2: ' + str(ob_2)
print 'same_yes: ' + str(same_yes2)
print 'same_no: ' + str(same_no2)
print 'num: ' + str(num2)
print 'Observed agreement3: ' + str(ob_3)
print 'same_yes: ' + str(same_yes3)
print 'same_no: ' + str(same_no3)
print 'num: ' + str(num3)
print 'Observed agreement4: ' + str(ob_4)
print 'same_yes: ' + str(same_yes4)
print 'same_no: ' + str(same_no4)
print 'num: ' + str(num4)
print 'Observed agreement5: ' + str(ob_5)
print 'same_yes: ' + str(same_yes5)
print 'same_no: ' + str(same_no5)
print 'num: ' + str(num5)
print 'Observed agreement6: ' + str(ob_6)
print 'same_yes: ' + str(same_yes6)
print 'same_no: ' + str(same_no6)
print 'num: ' + str(num6)

print 'Random agreement1: ' + str(rand_1)
print 'Random agreement2: ' + str(rand_2) 
print 'Random agreement3: ' + str(rand_3)
print 'Random agreement4: ' + str(rand_4)
print 'Random agreement5: ' + str(rand_5)
print 'Random agreement6: ' + str(rand_6)

print 'Result1: ' + str(result_1)
print 'Result2: ' + str(result_2)
print 'Result3: ' + str(result_3)
print 'Result4: ' + str(result_4)
print 'Result5: ' + str(result_5)
print 'Result6: ' + str(result_6)

