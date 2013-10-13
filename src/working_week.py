#!/usr/bin/env python
# $Id: working_week.py,v 1.1 2008/12/10 18:12:50 guest Exp $
#
# Call as working.py | working_week.py

import sys
import datetime

def main():
    haveData = False
    week = 0
    monday = None
    lastday = None

    for line in sys.stdin:
        date, hours = line.split()
        year, month, day = date.split('-')
        #print "xxx:", year, month, day, "->", hours
        day = datetime.date(int(year), int(month), int(day))
        if (day.weekday() == 0):
            # we have a Monday
            # do we have data for the last week?
            if (haveData):
                # yes, print it
                # monday is the last monday we save, lastday is the last day we summed up the hours
                print "From %s to %s -> %1.1f hours" % (monday, lastday, float(week) / 10)
            # we have data, so start to sum up the weekly work hours
            haveData = True
            week = int(hours)
            # save this Monday in var monday for the next print out
            monday = day
        elif (haveData):
            # we started to sum up weekly work hours
            week += int(hours)
            # and remember this day in var lastday used for print out
            lastday = day

if __name__ == "__main__":
    main()