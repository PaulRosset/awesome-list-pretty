#!/usr/bin/python
# coding: utf8

import sys
import getopt
import re
import json


def getData(filename="multObj.json"):
    dictionnary = {}
    file = open("readme.md", "r")
    title = ""
    for line in file:
        if line.split(" ")[0] == "##" and line.split(" ")[1] != "Contents\n" and line.split(" ")[1] != "License\n":
            getLine = line.split(" ")[1:]
            title = " ".join(getLine).replace("\n", "")
            dictionnary[title] = []
        if line.split(" ")[0] == "-" and title != "":
            matches = re.findall(
                "((\[[a-z\. &/`À-ÿ+\-A-Z0-9]*])(\([a-zA-Z]*.*?\))( - [a-zA-Z0-9].+?(?=\.))*)", line)
            if matches:
                for match in matches:
                    dictionnary[title].append({
                        "listName": re.sub("[\[^\[\]\]]", "", match[1]),
                        "url": re.sub("[\(^\(\)\)]", "", match[2]),
                        "desc": re.sub("^[ \- ]+", "", match[3])
                    })
    createFile(dictionnary, filename)
    file.close()


def getDataSingleObject(filename="singleObj.json"):
    dictionnary = []
    file = open("readme.md", "r")
    title = ""
    for line in file:
        if line.split(" ")[0] == "##" and line.split(" ")[1] != "Contents\n" and line.split(" ")[1] != "License\n":
            getLine = line.split(" ")[1:]
            title = " ".join(getLine).replace("\n", "")
        if line.split(" ")[0] == "-" and title != "":
            matches = re.findall(
                "((\[[a-z\. &/`À-ÿ+\-A-Z0-9]*])(\([a-zA-Z]*.*?\))( - [a-zA-Z0-9].+?(?=\.))*)", line)
            if matches:
                for match in matches:
                    dictionnary.append({
                        "listName": re.sub("[\[^\[\]\]]", "", match[1]),
                        "url": re.sub("[\(^\(\)\)]", "", match[2]),
                        "desc": re.sub("^[ \- ]+", "", match[3]),
                        "cat": title
                    })
    createFile(dictionnary, filename)
    file.close()


def createFile(dictionnary, filename):
    f = open(filename, "w+")
    f.write(json.dumps(dictionnary))
    f.close()


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
        opts["obj"] = getDataSingleObject
    elif opt == "-m":
        opts["obj"] = getData
    elif opt == "-f" and arg != "":
        opts["filename"] = arg

if 'filename' in opts:
    opts["obj"](opts["filename"])
else:
    opts["obj"]()
