#!/usr/bin/python
# coding: utf8

import re
import json
import urllib2


def getDataMultipleObject(file):
    dictionnary = {}
    title = ""
    for line in file:
        if line.split(" ")[0] == "##" and line.split(" ")[1] != "Contents\n" and line.split(" ")[1] != "License\n":
            getLine = line.split(" ")[1:]
            title = " ".join(getLine).replace("\n", "")
            dictionnary[title] = []
        if (line.split(" ")[0] == "-" or line.split(" ")[0] == "\t-" and title != "") and not re.match("(^- \[[a-z A-Z-0-9]+\]\(#[a-z0-9-]+\)$)", line):
            matches = re.findall(
                "((\[[a-z\. &/`À-ÿ+\-A-Z0-9]*])(\([a-zA-Z]*.*?\))( - [a-zA-Z0-9].+?(?=\.))*)", line)
            if matches:
                for match in matches:
                    dictionnary[title].append({
                        "listName": re.sub("[\[^\[\]\]]", "", match[1]),
                        "url": re.sub("[\(^\(\)\)]", "", match[2]),
                        "desc": re.sub("^[ \- ]+", "", match[3])
                    })
    return dictionnary


def getDataSingleObject(file):
    dictionnary = []
    title = ""
    for line in file:
        if line.split(" ")[0] == "##" and line.split(" ")[1] != "Contents\n" and line.split(" ")[1] != "License\n":
            getLine = line.split(" ")[1:]
            title = " ".join(getLine).replace("\n", "")
        if (line.split(" ")[0] == "-" or line.split(" ")[0] == "\t-" and title != "") and not re.match("(^- \[[a-z A-Z-0-9]+\]\(#[a-z0-9-]+\)$)", line):
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
    return dictionnary


def createFile(dictionnary, filename):
    f = open(filename, "w+")
    f.write(json.dumps(dictionnary))
    f.close()


def getDataFromUrlInFile(url):
    content = urllib2.urlopen(url).read()
    file = open("readme.md", "w+")
    file.write(content)
    file.close()


def main(method, filename="result.json", fileToOpen="readme.md"):
    getDataFromUrlInFile(
        "https://raw.githubusercontent.com/sindresorhus/awesome/master/readme.md")
    file = open(fileToOpen, "r")
    dic = getDataSingleObject(
        file) if method == 1 else getDataMultipleObject(file)
    createFile(dic, filename)
    file.close()


def verifyLength():
    file = open("readme.md", "r")
    print len(getDataSingleObject(file))
