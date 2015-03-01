#!/usr/bin/env python
# encoding: utf-8


fh = open('/Users/Yale/Desktop/ocr.html','r')
for line in fh:
    arr = ''
    for i in line:
        if i.isalpha() :
            arr = arr + i
    print(arr)
fh.close()

# new url is 'equality.html'

