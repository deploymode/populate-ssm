import json
import os
from typing import OrderedDict
from dotenv import dotenv_values
import argparse
import botocore
import boto3


def main():

    parser = argparse.ArgumentParser(description="Populate parameter store from .env and/or .json file")
    parser.add_argument("--env-file", required=False, help="Path to .env file")
    parser.add_argument("--json-file", required=False, help="Path to .json file containing an array of key/value objects")
    parser.add_argument(
        "paramStorePrefix", metavar="P", help="Path prefix for parameter store"
    )
    parser.add_argument(
        "--include",
        required=False,
        default="",
        help="Environment variables to include when writing. Excludes all others. CSV list, e.g. NODE_ENV,MY_VAR",
    )
    parser.add_argument(
        "--exclude",
        required=False,
        default="",
        help="Environment variables to exclude from writing. CSV list, e.g. NODE_ENV,MY_VAR",
    )

    args = parser.parse_args()

    env_values = OrderedDict()

    if args.env_file:
        print("Loading env vars from {}".format(args.env_file))
        try:
            env_values = dotenv_values(dotenv_path=args.env_file)
        except IOError:
            print(".env file does not exist")


    if args.json_file:
        print("Loading env vars from {}".format(args.json_file))
        env_values.update(load_env_vars_from_json(args.json_file))

    if not env_values:
        print("Nothing to write")
        return

    env_vars_to_include = []
    env_vars_to_exclude = []

    if len(args.include) > 0:
        env_vars_to_include = args.include.split(",")
        print("Including: {}".format("; ".join(env_vars_to_include)))

    if len(args.exclude) > 0:
        env_vars_to_exclude = args.exclude.split(",")
        print("Excluding: {}".format("; ".join(env_vars_to_exclude)))

    client = boto3.client("ssm")

    for key, value in env_values.items():
        if len(env_vars_to_include) > 0 and key not in env_vars_to_include:
            continue

        if key in env_vars_to_exclude:
            print("Skipping {}".format(key))
            continue

        if not value or len(value) == 0:
            print("Skipping {} due to empty value".format(key))
            continue

        paramPath = "{}/{}".format(args.paramStorePrefix, key)
        try:
            response = client.put_parameter(
               Name=paramPath, Value=value, Type="SecureString", Overwrite=True
            )
        except botocore.exceptions.ClientError as e:
            print(e)
            print("AWS client error - do you have valid tokens set in the env?")
            return

        # print(response)
        if response["ResponseMetadata"]["HTTPStatusCode"] == 200:
            print("Wrote {}".format(paramPath))
        else:
            print("Failed to write {}".format(paramPath))

    print("Done")

def load_env_vars_from_json(json_file_path):
    if not os.path.exists(json_file_path):
        print("JSON file path does not exist")
        return OrderedDict([])

    f = open(json_file_path)

    json_data = json.load(f)

    f.close()

    data = [(k, d[k]) for d in json_data for k in d]

    return OrderedDict(data)


if __name__ == "__main__":
    main()
