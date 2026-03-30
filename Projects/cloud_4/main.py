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

"""Obtain bucket size."""

import argparse
import sys
import boto3
from botocore.exceptions import ClientError


def parse_args() -> tuple[str, str]:
        """Get arguments as input.

        Args: None => reads from arguments with argparse.

        Returns: Bucket name and optionally an object name. 
        """
        cli_parser = argparse.ArgumentParser(
                prog = "python3 main.py",
                description = "s3 bucket size"
        )
        cli_parser.add_argument("--bucket", required=True, help="get bucket name")
        cli_parser.add_argument("--prefix", default="", help="get object name")
        args = cli_parser.parse_args()
        return args.bucket, args.prefix


def get_bucket_stats(bucket: str, prefix: str) -> tuple[int, int]:
        """Returns total bucket size and total object count.
        
        Args:
                bucket: The given s3 bucket.
                prefix: The key for a particular object.
        
        Returns: Total object count and bucket size 
        """
        client = boto3.client("s3")
        paginator = client.get_paginator("list_objects_v2")
        pages = paginator.paginate(Bucket=bucket, Prefix=prefix)
        s3_objects: list[dict] = []
        for page in pages:
                s3_objects.extend(page.get("Contents", []))
        object_count: int = len(s3_objects)
        bucket_size: int = 0
        for s3_object in s3_objects:
                bucket_size += s3_object["Size"]
        return object_count, bucket_size


def format_size(bucket_size: int) -> str:
        """Converts the stats into required output format.
        
        Args:
                bucket_size: Total bucket size.

        Returns: The size in required format.
        """
        size: str = ""
        if bucket_size < 1024:
                size = f"{bucket_size} B"
        elif bucket_size < (1024 ** 2):
                size = f"{(bucket_size / 1024):.2f} KB"
        elif bucket_size < 1024 ** 3:
                size = f"{(bucket_size / 1024 ** 2):.2f} MB"
        else:
                size = f"{(bucket_size / 1024 ** 3):.2f} GB"
        return size


def main() -> None:
        """Returns total objects count and total size."""
        bucket, prefix = parse_args()
        try:
                object_count, bucket_size = get_bucket_stats(bucket, prefix)
                if object_count == 0:
                        print("Bucket is empty.")
                        sys.exit(0)
        except ClientError as Error:
                print(f"ClientError: {Error}", file=sys.stderr)
                sys.exit(1)
        bucket_size_formatted: str = format_size(bucket_size)
        print(f"Bucket: {bucket}\nObjects: {object_count}\nSize: {bucket_size_formatted}")


if __name__ == "__main__":
        main()