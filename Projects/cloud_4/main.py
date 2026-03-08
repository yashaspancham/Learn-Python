# Cloud Storage Space Checker
# Reports the total size of an S3 bucket in human-readable format.
#
# Usage:
#   python main.py --bucket my-bucket-name
#   python main.py --bucket my-bucket-name --prefix logs/
#
# Output:
#   Bucket:   my-bucket-name
#   Objects:  1,024
#   Size:     3.72 GB
#
# Boto3 reference:
#   client = boto3.client("s3")
#   paginator = client.get_paginator("list_objects_v2")
#   pages = paginator.paginate(Bucket=bucket, Prefix=prefix)
#   each page has "Contents" (list of object dicts) — may be absent if page is empty
#   object fields: "Key" (str), "Size" (int, bytes)
#   use a paginator because list_objects_v2 returns max 1000 objects per call
#
# Size formatting:
#   bytes < 1024          → "{n} B"
#   bytes < 1024**2       → "{n:.2f} KB"
#   bytes < 1024**3       → "{n:.2f} MB"
#   else                  → "{n:.2f} GB"
#
# argparse reference:
#   --bucket: required, the S3 bucket name
#   --prefix: optional, default "" (empty string), filter objects by key prefix
#
# Environment:
#   AWS credentials must be set via `aws configure` or environment variables.
#
# Error cases to handle:
#   - botocore.exceptions.ClientError  → print to stderr, exit 1
#   - Bucket is empty (0 objects) → print "Bucket is empty." and exit 0


# TODO: import stdlib modules (sys, argparse)
# TODO: import boto3 and botocore exceptions


# TODO: write parse_args() -> tuple[str, str]
#       parses --bucket (required) and --prefix (optional, default "")
#       returns (bucket, prefix)


# TODO: write get_bucket_stats(bucket: str, prefix: str) -> tuple[int, int]
#       uses a paginator to iterate all objects
#       accumulates total object count and total size in bytes
#       returns (object_count, total_bytes)


# TODO: write format_size(total_bytes: int) -> str
#       converts bytes to human-readable string (B, KB, MB, GB)
#       returns formatted string


# TODO: write main() -> None
#       calls parse_args and get_bucket_stats
#       prints bucket name, object count, and formatted size
#       handles ClientError and empty bucket
