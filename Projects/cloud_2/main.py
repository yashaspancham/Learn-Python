# EC2 Instance Lister
# Lists all running EC2 instances across a region and prints their ID, type, and state.
#
# Usage:
#   python main.py
#   python main.py --region us-west-2
#   python main.py --state stopped
#
# Output (one line per instance):
#   i-0abc123def456  t2.micro   running   us-east-1a
#   i-0xyz789ghi012  t3.small   running   us-east-1b
#
# Boto3 reference:
#   client = boto3.client("ec2", region_name=region)
#   response = client.describe_instances(Filters=[{"Name": "instance-state-name", "Values": [state]}])
#   response["Reservations"] is a list of reservation dicts
#   each reservation["Instances"] is a list of instance dicts
#   instance fields: "InstanceId", "InstanceType", "State" (dict with "Name"), "Placement" (dict with "AvailabilityZone")
#
# argparse reference:
#   --region: optional, default "us-east-1"
#   --state:  optional, default "running", choices: running | stopped | all
#             when "all", do NOT pass a state filter to describe_instances
#
# Environment:
#   AWS credentials must be set via `aws configure` or environment variables.
#   Region in --region overrides AWS_DEFAULT_REGION env var.
#
# Error cases to handle:
#   - botocore.exceptions.ClientError  → print to stderr, exit 1
#   - botocore.exceptions.NoRegionError → print helpful message, exit 1
#   - No instances found → print "No instances found." and exit 0


# TODO: import stdlib modules (argparse, sys)
# TODO: import boto3 and botocore exceptions


# TODO: write parse_args() -> tuple[str, str]
#       parses --region and --state
#       returns (region, state)


# TODO: write list_instances(region: str, state: str) -> list[dict]
#       calls describe_instances with correct filters
#       flattens reservations → instances
#       returns list of instance dicts


# TODO: write format_instance(instance: dict) -> str
#       extracts InstanceId, InstanceType, State["Name"], Placement["AvailabilityZone"]
#       returns a tab-separated string


# TODO: write main() -> None
#       calls parse_args, list_instances, prints formatted output
#       handles ClientError and NoRegionError
#       prints "No instances found." if list is empty
"""EC2 Instance Lister: lists running EC2 instances by region and state."""


import sys
import argparse
import boto3
from botocore.exceptions import ClientError


def parse_args() -> tuple[str, str]:
        """
        Parse and validate CLI arguments

        Args:
                None - reads from sys.argv directly via argparse.
        
        Returns:
                A tuple of region and state.

        Raises:
                SystemExit: if arguments are invalid.
        """
        parser = argparse.ArgumentParser(
                prog = "python3 main.py",
                description = "List EC2 instances"
        )
        parser.add_argument("--region", default="us-east-1", help="AWS region to list instances in")
        parser.add_argument("--state", default="all", help="Instance state to filter by")
        args = parser.parse_args()
        if args.state not in ["all", "running", "stopped"]:
                print("Error: State argument is invalid")
                sys.exit(1)
        return args.region, args.state


def format_instance(instances: list[dict], region: str, state: str) -> list[str]:
        """
        Format response["Reservations"] into instance_id instance_type instance_state region.

        Args:
                instances: List of instances info.
                state: Required state of ec2 instances.
                region: AWS region to check ec2 instances for.  
        
        Returns:
                required_format: list of strings in the required format.
        """
        required_format: list[str] = []
        instances_only = [instance["Instances"] for instance in instances]
        instance_datalist: list[dict] = []
        for instance_reservation in instances_only:
                instance_datalist.extend(instance_reservation)
        for instance_info in instance_datalist:
                required_format.append(f"{instance_info["InstanceId"]}\t {instance_info["InstanceType"]}\t {instance_info["State"]["Name"]}\t {region}")

        return required_format


def main() -> None:
        """Prints all the ec2 instances in region with the specified state."""
        region, state = parse_args()
        client = boto3.client("ec2", region_name=region)
        if state == "all":
                response = client.describe_instances()
        else:
                response = client.describe_instances(Filters=[{"Name": "instance-state-name", "Values": [state]}])
        ec2_reservations = response["Reservations"]
        ec2_info_list = format_instance(ec2_reservations, region, state)
        if not ec2_info_list:
                print("No instances found.")
                sys.exit(0)
        for ec2_info in ec2_info_list:
                print(ec2_info)


if __name__ == "__main__":
        try:
                main()
        except ClientError as e:
                print(e, file=sys.stderr)
                sys.exit(1)