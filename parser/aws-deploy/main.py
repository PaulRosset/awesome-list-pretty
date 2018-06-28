#!/usr/bin/python

import json
from indexEntry import cleanBeforeFilling, pushNewIndexs


def lambda_handler(event, context):
    resClean = cleanBeforeFilling()
    resPush = pushNewIndexs()
    if resClean == "done" and resPush == "done":
        return {
            "statusCode": 200,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({"status": "Done!"})
        }
    else:
        return {
            "statusCode": 500,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({"status": "KO", "CleanStatus": resClean, "PushStatus": resPush})
        }
