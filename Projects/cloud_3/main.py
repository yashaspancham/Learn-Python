# IAM User Auditor
# Lists all IAM users in the account and their last console login date.
#
# Usage:
#   python main.py
#   python main.py --never-logged    (show only users who never logged in)
#
# Output (one line per user):
#   alice        us-east-1   2024-01-15   2025-02-10
#   bob          us-east-1   2023-06-01   Never
#
# Boto3 reference:
#   client = boto3.client("iam")
#   response = client.list_users()
#   response["Users"] is a list of user dicts
#   user fields: "UserName", "UserId", "CreateDate" (datetime), "PasswordLastUsed" (datetime, may not exist)
#   use user.get("PasswordLastUsed") — returns None if user never logged in via console
#   dates are datetime objects; format with .strftime("%Y-%m-%d")
#
# argparse reference:
#   --never-logged: optional flag (store_true), filters to users where PasswordLastUsed is missing
#
# Environment:
#   AWS credentials must be set via `aws configure` or environment variables.
#   IAM is a global service — no region needed.
#
# Error cases to handle:
#   - botocore.exceptions.ClientError  → print to stderr, exit 1
#   - No users found → print "No users found." and exit 0


# TODO: import stdlib modules (sys, argparse)
# TODO: import boto3 and botocore exceptions


# TODO: write parse_args() -> bool
#       parses --never-logged flag
#       returns True if flag is set, False otherwise


# TODO: write list_users() -> list[dict]
#       calls iam.list_users()
#       returns response["Users"]


# TODO: write format_user(user: dict) -> str
#       extracts UserName, CreateDate, PasswordLastUsed
#       formats dates as YYYY-MM-DD strings
#       if PasswordLastUsed is None, use "Never"
#       returns a tab-separated string


# TODO: write main() -> None
#       calls parse_args and list_users
#       if --never-logged, filter users where PasswordLastUsed is missing
#       formats and prints each user
#       handles ClientError and empty list
