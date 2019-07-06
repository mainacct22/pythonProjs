# coding=utf-8
import unicodedata
title = u'Klüft skräms inför på fédéral électoral große'
t = title.encode('utf-8').decode('unicode-escape')
print(t)
unicodedata.normalize('NFKD', title).encode('ascii','ignore')
print(title)
