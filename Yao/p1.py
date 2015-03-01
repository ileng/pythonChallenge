#!/usr/bin/env python
# encoding: utf-8


import string

text = """g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."""
src = string.ascii_lowercase
dst = string.ascii_lowercase[2:] + string.ascii_lowercase[0:2]

transtab = string.maketrans(src, dst)
print text.translate(transtab)
