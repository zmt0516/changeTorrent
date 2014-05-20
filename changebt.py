#!/usr/bin/env python

import transpy
import bencode
import sys

def changebt(bts):
    try:
        bd=bencode.bdecode(bts)
    except:
        print 'Can not open the torrent string.'
        return bts
    try:
        for i in ['publisher', 'piece length', 'publisher.utf-8', 'publisher-url.utf-8', 'publisher-url']:
            bd['info'][i]=''
        for i in ['name','name.utf-8']:
            ## If U can not use the torrent also, add the code next line
            #bd['info'][i]=transpy.getpinyin(bd['info'][i])
            pass
        filelist=bd['info']['files']
        fl=[[i['length'],i] for i in filelist]
        fl=[max(fl)[1]]
        fl2=[i for i in filelist if i['length']>100*1024]
        if len(fl2)!=0:
            bd['info']['files']=fl2
        else:
            bd['info']['files']=fl
    except:
        print 'Can not tanslate the torrent string.'
        return bts
    return bencode.bencode(bd)

if __name__=='__main__':
    try:
        fn=sys.argv[1]
        bts=open(fn).read()
    except:
        print 'U need use it as: python changebt.py xyz.torrent.'
        pass
    bts=changebt(bts)
    fnl=fn.split('.')
    fnl=fnl[:-1]+['new']+fnl[-1:]
    fnl='.'.join(fnl)
    open(fnl,'w').write(bts)

    
    
