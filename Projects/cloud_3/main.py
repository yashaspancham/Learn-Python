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
"""Lists all users"""


import argparse
import sys
import boto3
from botocore.exceptions import ClientError


def never_logged_users(users: list[dict]) -> list[dict]:
        """Filters users who never loggedin.
        
        Args: 
                users: List all the users.
        
        Returns: List of users who never loggedin.
        """
        never_logged_users_list: list[dict] = []
        for user in users:
                if user.get("PasswordLastUsed") is None:
                        never_logged_users_list.append(user)
        return never_logged_users_list


def list_users(client: 'botocore.client.IAM', never_logged_flag: bool) -> list[dict]:
        """Lists users based on never_logged_flag.
        
        Args:
                client: boto3's IAM class.
                never_logged_flag: flag for --never-logged.
        
        Returns: List of users.
        """
        response = client.list_users()
        if never_logged_flag:
                return never_logged_users(response["Users"])
        else:
                return response["Users"]


def format_user(users: list[dict]) -> list[str]:
        """Converts the list of users to list of users in the required format.
        
        Args:
                users: List of users.
        
        Returns: List of users in the required format.
        """
        format_user_list: list[str] = []
        for user in users:
                user_name: str = user["UserName"]
                user_creation_date: str = user["CreateDate"].strftime("%Y-%m-%d")
                user_last_password_used: str = user["PasswordLastUsed"].strftime("%Y-%m-%d") if user.get("PasswordLastUsed") else "Never"
                format_user_list.append(f"{user_name}\t{user_creation_date}\t{user_last_password_used}")
        return format_user_list


def parse_arguments() -> bool:
        """Get arguments as input.
        
        Args: None => reads from arguments with argparse.

        Returns: Flag for --never-logged.
        """
        cli_parser = argparse.ArgumentParser(
                prog = "python3 main.py",
                description = "List users and last login."
        )
        cli_parser.add_argument("--never-logged", action="store_true", help="list users who never logged-in.")
        args = cli_parser.parse_args()

        return args.never_logged


def main() -> None:
        """Prints all the users in a required format."""
        never_logged_flag: bool = parse_arguments()
        client = boto3.client("iam")
        users = list_users(client, never_logged_flag)
        if not users:
                print("No users found.")
                sys.exit(0)
        users_format = format_user(users)
        for user in users_format:
                print(user)


if __name__ == "__main__":
        try:
                main()
        except ClientError as e:
                print(e, file=sys.stderr)
                sys.exit(1)