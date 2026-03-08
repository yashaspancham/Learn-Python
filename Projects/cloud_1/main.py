import argparse
import sys
from dotenv import load_dotenv
from s3_client import upload_file

load_dotenv()


def parse_bucket_target(target: str) -> tuple[str, str | None]:
    """
    Parse a bucket target string into a bucket name and optional key.

    Args:
        target: A string in the format "bucket" or "bucket:key".

    Returns:
        A tuple of (bucket, key) where key may be None.
    """
    if ":" in target:
        bucket, key = target.split(":", 1)
        return bucket, key
    return target, None


def parse_args() -> tuple[str, str, str | None]:
    """
    Parse and validate CLI arguments.

    Args:
        None — reads from sys.argv directly via argparse.

    Returns:
        A tuple of (file_path, bucket, key) where key may be None.

    Raises:
        SystemExit: If required arguments are missing.
    """
    parser = argparse.ArgumentParser(
        prog="s3up",
        description="Upload a file to AWS S3",
    )
    parser.add_argument("file", help="Path to the file to upload")
    parser.add_argument("target", help="S3 destination in the format bucket or bucket:key")
    args = parser.parse_args()

    bucket, key = parse_bucket_target(args.target)
    return args.file, bucket, key


def main() -> None:
    """Parse CLI input and upload the specified file to S3."""
    file_path, bucket, key = parse_args()

    try:
        uri = upload_file(file_path, bucket, key)
        print(f"Upload successful: {uri}")
    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except RuntimeError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
