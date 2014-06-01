#!/usr/bin/env python

import transpy
import bencode
import sys

def changebted2k(bts):
    try:
        bd=bencode.bdecode(bts)
    except:
        print 'Can not open the torrent string.'
        return []
    try:
        ed2k=[]
        filist=[(i['length'],i) for i in bd['info']['files']]
        filist.sort()
        filist.reverse()
        filist=[i[1] for i in filist]
        for i in filist:
            try:
                ed2k+=['ed2k://|file|'+i['path'][-1]+'|'+str(i['length'])+'|'+''.join([ ('%02X'% ord(j)) for j in i['ed2k']])+'|/']
            except:
                pass
    except:
        print 'Can not tanslate the torrent string.'
        return []
    return ed2k

if __name__=='__main__':
    try:
        fn=sys.argv[1]
        bts=open(fn).read()
    except:
        print 'U need use it as: python changebt.py xyz.torrent.'
        pass
    ed2k=changebted2k(bts)
    for i in ed2k:
        print i
    
    
    
