#!/usr/bin/env python
import boto3
import argparse
import yaml
import os

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("job_data", type=str)
    parser.add_argument("--aws_auth_method", type=str, default="iam")
    parser.add_argument("--topic_arn", type=str, default="")
    return parser.parse_args()

def main():
    args = parse_args()
    with open(args.job_data, mode='r') as f:
        message = f.read()

    if args.aws_auth_method == "keys":
        sts_client = boto3.client('sts', region_name='us-west-2',
                              aws_access_key_id = os.getenv("ACCESS_KEY"),
                              aws_secret_access_key = os.getenv("SECRET_KEY"),
                              aws_session_token = os.getenv("SESSION_TOKEN"))
        print(sts_client.get_caller_identity())
        client = boto3.client('sns', region_name='us-west-2',
                              aws_access_key_id = os.getenv("ACCESS_KEY"),
                              aws_secret_access_key = os.getenv("SECRET_KEY"),
                              aws_session_token = os.getenv("SESSION_TOKEN"))

    elif args.aws_auth_method == "iam":
        sts_client = boto3.client('sts', region_name='us-west-2')
        print(sts_client.get_caller_identity())
        client = boto3.client('sns', region_name='us-west-2')

    else:
        print(f"Invalid aws_auth_method: {args.aws_auth_method}")
        print(f"Supported methods: iam, keys")
        exit()

    with open(args.job_data, mode='r') as f:
        message = f.read()
    
    if not args.topic_arn:
        topic_arn = f"arn:aws:sns:{sts_client.meta.region_name}:{sts_client.get_caller_identity()['Account']}:unity-sps-job-status.fifo"
    else:
        topic_arn = args.topic_arn

    print(client.publish(
        TopicArn=topic_arn,
        Message=message,
        MessageGroupId="jobstatus"
    ))

if __name__ == "__main__":
    main()