#!/usr/bin/python

import json
from indexEntry import cleanBeforeFilling, pushNewIndexs


def lambda_handler(event, context):
    resClean = cleanBeforeFilling()
    resPush = pushNewIndexs()
    if resClean == "done" and resPush == "done":
        return json.dumps({
            "statusCode": 200,
            "headers": {"Content-Type": "application/json"},
            "body": {"status": "Done!"}
        })
    else:
        return json.dumps({
            "statusCode": 500,
            "headers": {"Content-Type": "application/json"},
            "body": {"status": "KO", "CleanStatus": resClean, "PushStatus": resPush}
        })
