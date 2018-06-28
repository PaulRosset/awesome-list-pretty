#!/usr/bin/python

import os
from algoliasearch import algoliasearch
from parser import getDataFromUrlInFile, getDataSingleObject

client = algoliasearch.Client(
    os.environ["APPID_ALGOLIA"], os.environ["APIKEY_ALGOLIA"])
index = client.init_index(os.environ["INDEX_ALGOLIA"])


def cleanBeforeFilling():
    try:
        ids = []
        res = index.browse_all({"query": ""})
        for hit in res:
            ids.append(hit["objectID"])
        index.delete_objects(ids)
        return "done"
    except Exception as e:
        return str(e)


def pushNewIndexs():
    try:
        getDataFromUrlInFile(
            "https://raw.githubusercontent.com/sindresorhus/awesome/master/readme.md")
        file = open("readme.md", "r")
        res = getDataSingleObject(file)
        index.add_objects(res)
        file.close()
        return "done"
    except Exception as e:
        return str(e)
