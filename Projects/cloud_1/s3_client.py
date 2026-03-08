import os
import boto3
from botocore.exceptions import ClientError


def is_s3_folder(s3_client, bucket: str, key: str) -> bool:
    """Check if a key is an existing folder prefix in S3.
    
    Args:
        s3_client: An initialized boto3 S3 client.
        bucket: The S3 bucket name.
        key: The key to check.

    Returns:
        True if the key is an existing folder prefix, False otherwise.
    """
    response = s3_client.list_objects_v2(Bucket=bucket, Prefix=key + "/", MaxKeys=1)
    return "Contents" in response


def upload_file(file_path: str, bucket: str, object_name: str | None = None) -> str:
    """Upload a file to S3 and return its URI.
    
    Args:
        file_path: The path to the file to upload.
        bucket: The S3 bucket name.
        object_name: The key under which to store the file in S3. If None, uses the file name.

    Returns:
        The S3 URI of the uploaded file.

    Raises:
        FileNotFoundError: If the specified file does not exist.
        RuntimeError: If the upload fails.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    s3 = boto3.client("s3")

    if object_name is None:
        object_name = os.path.basename(file_path)
    elif object_name.endswith("/"):
        object_name = object_name + os.path.basename(file_path)
    elif is_s3_folder(s3, bucket, object_name):
        object_name = object_name + "/" + os.path.basename(file_path)

    try:
        s3.upload_file(file_path, bucket, object_name)
    except ClientError as e:
        raise RuntimeError(f"Upload failed: {e}") from e

    return f"s3://{bucket}/{object_name}"