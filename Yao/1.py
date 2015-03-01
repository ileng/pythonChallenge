#!/usr/bin/env python
# encoding: utf-8
import string

a = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
a = 'map'
b = ''
for i in a:
    if i.isalpha() :
        ix = string.lowercase.index(i)
        i =  string.lowercase[(ix+2)%26]
    b = b + i
print(b)

# get the url as ocr.html


