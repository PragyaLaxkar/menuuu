
# import boto3
# import cgi
# import os
# import json
# import sys
# print("Content-type: text/html")
# print()

# form = cgi.FieldStorage()
# img = form.getvalue("image")

# ec2 = boto3.resource(
#         "ec2",
#         aws_access_key_id="AKIAUANBPEQ4SN2QBZ64",
#         aws_secret_access_key="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",
#         region_name='ap-south-1'
#     )
# instance = ec2.create_instances(    
#         ImageId=img,
#         MinCount=1,
#         MaxCount=1,
#         InstanceType="t2.micro",
#     )
# print(instance)

#!/usr/bin/python3
import boto3
import cgi
import os
import sys

print("Content-type: text/html")
print()

form = cgi.FieldStorage()
img = form.getvalue("image")

if not img:
    print("<b>No image name provided</b>")
    sys.exit()

image_mapping = {
    "Amazon": "ami-0e1d06225679bc1c5",
    "amazon": "ami-0e1d06225679bc1c5",
    "Redhat9": "ami-022ce6f32988af5fa",
    "redhat9": "ami-022ce6f32988af5fa",
    "Ubuntu": "ami-0f58b397bc5c1f2e8",
    "ubuntu": "ami-0f58b397bc5c1f2e8"
}

if img not in image_mapping:
    print("<b>Invalid image name</b>")
    sys.exit()

image_id = image_mapping[img]

try:
    ec2 = boto3.resource(
        "ec2",
        aws_access_key_id=os.environ.get("AKIAUANBPEQ4SN2QBZ64"),
        aws_secret_access_key=os.environ.get("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"),
        region_name='ap-south-1'
    )

    instance = ec2.create_instances(
        ImageId=image_id,
        MinCount=1,
        MaxCount=1,
        InstanceType="t2.micro",
    )
    instance_id = instance[0].id
    print(f"<b>EC2 INSTANCE LAUNCHED ........!</b><br/>Instance id is: {instance_id}")

except Exception as e:
    print(f"<b>Failed to launch instance:</b> {str(e)}")
