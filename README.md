- create IAM role with S3 Access(read-only for source bucket / write only for output bucket)
- zip and upload as lambda layer necessary python packages(venv/lib/python3.9/site-packages/)
- set role and layers on lambda
- increase default 3s lambda timeout to ~10s(configuration/general configuration/timeout)
- add s3 upload trigger on lambda