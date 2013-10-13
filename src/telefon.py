#!/usr/bin/env python
# $Id$
#
# Usage: ./telefon.py $HOME/Wissen/telefon.txt <pattern>

import re
import sys

# pats holds the list of regex patterns to search for
pats = list()

# linePat is the delimiter between entries
linePat = re.compile("^---")

# we need at least the file and one pattern
if len(sys.argv) <= 2:
    print """
    Usage: telefon.py <telefon> <pattern_1> <pattern_2> ...  <pattern_n>
       where <pattern_i> is a regular expression like "ul.*"
       The patterns are ANDed, so you can search for that:
       ./telefon.py telefon.txt klaus "ul.*"
       and you are searching for klaus (case does not matter) AND 
       any word starting with ul 
        """
    sys.exit(1)

# The file is the first argument
file = sys.argv[1]
for i in sys.argv[2:]:
    # the next arguments are regex patterns, we ignore case
    pats.append(re.compile(i, re.IGNORECASE))

# Do the job
def run():
    # Reset text to none
    text = None
    for line in open(file, "r"):
        # do we have a line pattern?
        if linePat.search(line):
            # first or next entry found
            if not text:
                # first entry
                text = ""
            else:
                # entry ended -> search for pattern, text contains the data to search for
                # set found marker
                found = True
                for p in pats:
                    match = p.search(text)
                    if (match):
                        # yes, we have a match
                        found &= True
                    else:
                        # no match, reset found marker to False
                        found = False
                if found:
                    # all the pattern did match with the text, print it
                    print "%s" %(79*"-")
                    print "%s" % text,
                # we finished the entry and need to reset text
                text = ""
        elif text is not None:
            # we are not at a line delimiter, so we need to collect data in var text
            text += line

if __name__ == "__main__":
    run()
