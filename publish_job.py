#!/usr/bin/env python
import boto3
import argparse
import json
import os


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--job_id", type=str, default="", help="Job ID of job being executed"
    )
    parser.add_argument(
        "--job_status", type=str, default="", help="Status of job being executed"
    )
    parser.add_argument(
        "--job_inputs",
        type=str,
        default="[]",
        help="JSON array of WPS-T job input objects associated with job",
    )
    parser.add_argument(
        "--job_outputs",
        type=str,
        default="[]",
        help="JSON array of WPS-T job output objects associated with job",
    )
    parser.add_argument(
        "--tags",
        type=str,
        default="{}",
        help="JSON array of WPS-T job output objects associated with job",
    )
    parser.add_argument("--aws_auth_method", type=str, default="iam")
    parser.add_argument("--topic_arn", type=str, default="")

    return parser.parse_args()


def get_sts_and_sns_clients(aws_auth_method):
    if aws_auth_method == "keys":
        sts_client = boto3.client(
            "sts",
            region_name="us-west-2",
            aws_access_key_id=os.getenv("ACCESS_KEY"),
            aws_secret_access_key=os.getenv("SECRET_KEY"),
            aws_session_token=os.getenv("SESSION_TOKEN"),
        )
        print(sts_client.get_caller_identity())
        client = boto3.client(
            "sns",
            region_name="us-west-2",
            aws_access_key_id=os.getenv("ACCESS_KEY"),
            aws_secret_access_key=os.getenv("SECRET_KEY"),
            aws_session_token=os.getenv("SESSION_TOKEN"),
        )

    elif aws_auth_method == "iam":
        sts_client = boto3.client("sts", region_name="us-west-2")
        print(sts_client.get_caller_identity())
        client = boto3.client("sns", region_name="us-west-2")

    else:
        print(f"Invalid aws_auth_method: {aws_auth_method}")
        print(f"Supported methods: iam, keys")
        exit()

    return sts_client, client


def main():
    args = parse_args()

    # get sts and sns aws clients
    sts_client, sns_client = get_sts_and_sns_clients(args.aws_auth_method)

    # contstruct final job data json object
    job_data = {
        "id": args.job_id,
        "inputs": args.job_inputs,
        "outputs": args.job_outputs,
        "tags": args.tags,
        "status": args.job_status,
    }

    if not args.topic_arn:
        topic_arn = os.getenv("JOBS_DATA_SNS_TOPIC_ARN")
    else:
        topic_arn = args.topic_arn

    print(
        sns_client.publish(
            TopicArn=topic_arn, Message=json.dumps(job_data), MessageGroupId=args.job_id
        )
    )


if __name__ == "__main__":
    main()
