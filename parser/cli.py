#!/usr/bin/python
# coding: utf8

import getopt
import sys

from parser import main

try:
    opts = {}
    optOr = 0
    optlist, args = getopt.getopt(sys.argv[1:], "smf:")
    for opt, arg in optlist:
        if opt == "-s" or opt == "-m":
            optOr += 1
    if optOr > 1 or optOr == 0:
        raise getopt.GetoptError("Error", "Argument -s|-m ")
except getopt.GetoptError:
    print "Usage: parse.py -s(SingleObject)|-m(MultipleObject) -f <filename>"
    sys.exit(2)
for opt, arg in optlist:
    if opt == "-s":
        opts["method"] = 1
    elif opt == "-m":
        opts["method"] = 0
    elif opt == "-f" and arg != "":
        opts["filename"] = arg

if 'filename' in opts:
    main(opts["method"], opts["filename"])
else:
    main(opts["method"])
