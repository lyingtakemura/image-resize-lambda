import json
import os
from urllib.parse import unquote_plus

import boto3
from PIL import Image

s3 = boto3.client("s3")

def lambda_handler(event, context):
    for record in event["Records"]:
        bucket = record["s3"]["bucket"]["name"]
        key = unquote_plus(record["s3"]["object"]["key"])
        response = s3.get_object(Bucket=bucket, Key=key)
        content = response["Body"]
        # print(content)
        with Image.open(content) as obj:
            print(obj.size)
            name = "/tmp/resized-testimg.jpg"
            result = obj.resize((512, 512), Image.Resampling.LANCZOS)

            try:
                result.save(name, quality=50)
            except Exception as e:
                print(e)
        print(os.listdir("/tmp/"))
        s3.upload_file(
            "/tmp/resized-testimg.jpg", "socmed-sample", "resized-testimg.jpg"
        )

        return {"statusCode": 200, "body": json.dumps("ok")}
