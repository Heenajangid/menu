#!/usr/bin/env python3

import cgi
import cgitb
import boto3
from botocore.exceptions import ClientError

cgitb.enable()

print("Content-Type: text/html")
print()

form = cgi.FieldStorage()

region = form.getvalue('region')
instance_type = form.getvalue('instance_type')
ami_id = form.getvalue('ami_id')
key_name = form.getvalue('key_name')
access_key = form.getvalue('access_key')
secret_key = form.getvalue('secret_key')


html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Launch EC2 Instance</title>
</head>
<body>
"""

try:
    ec2 = boto3.client(
        'ec2',
        region_name=region,
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key
    )
    response = ec2.run_instances(
        ImageId=ami_id,
        InstanceType=instance_type,
        KeyName=key_name,
        MinCount=1,
        MaxCount=1
    )

    instance_id = response['Instances'][0]['InstanceId']
    html += f"<p>Instance launched successfully! Instance ID: {instance_id}</p>"

except ClientError as e:
    html += f"<p>Error launching instance: {e}</p>"

html += """
</body>
</html>
"""

print(html)
