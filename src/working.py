#!/usr/bin/env python3

import os
import sys
import datetime

FILE_EXT = 'Wissen' + os.sep + 'working.txt'
DB = os.getenv('HOME', 'c:/tmp')
FILE = DB + os.sep + FILE_EXT

def calc():
    dict = read_data()
    keys = list(dict.keys())
    keys.sort()
    for k in keys:
        print("%s %3.1d" % (k, dict.get(k))) 
#    for k, v in dict.iteritems():
#        print k, v 

def read_data():
    d = {}
    for i in open(FILE):
        if i.find('#') == 0:
            continue 
        date, value = i.strip().split()
        v = int(value)
        #print("XXX: ", date,'->', v)
        if date in d:
            d[date] = d[date] + v
        else:
            d[date] = v
        print('Now: ', date, '->', d[date])
    return d

def main():
    arg = 0
    d = datetime.date.today()
    if len(sys.argv) > 1:
        arg = sys.argv[1]
        
    if arg > 0:
        out = open(FILE, 'a')
        out.write("%s %s\n" % (d, arg))
    else: 
        calc()
    
if __name__ == '__main__':
    main()
