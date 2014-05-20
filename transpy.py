#!/usr/bin/env python

import pinyin

test=pinyin.PinYin()
test.load_word()
def getpinyin(s):
    s2=''
    try:
        s=s.decode('utf8')
    except:
        pass
    for i in s:
        try:
            si=test.hanzi2pinyin(string=i)[0]
            if si=='':
                si=i
        except:
            si=i

        s2+=si
    return s2.encode('utf8')
