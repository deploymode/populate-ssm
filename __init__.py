from dotenv import dotenv_values
import argparse
import boto3


parser = argparse.ArgumentParser(description='Populate parameter store')
parser.add_argument('envFilePath', metavar='E', help='Path to .env file')
parser.add_argument('paramStorePrefix', metavar='P',
                    help='Path prefix for parameter store')
parser.add_argument('--include', required=False, default='',
                    help='Environment variables to include when writing. Excludes all others. CSV list, e.g. NODE_ENV,MY_VAR')
parser.add_argument('--exclude', required=False, default='',
                    help='Environment variables to exclude from writing. CSV list, e.g. NODE_ENV,MY_VAR')

args = parser.parse_args()

print('Loading env vars from {}'.format(args.envFilePath))

env_path = args.envFilePath
env_values = dotenv_values(dotenv_path=env_path)

env_vars_to_include = []
env_vars_to_exclude = []

if len(args.include) > 0:
    env_vars_to_include = args.include.split(",")
    print('Including: {}'.format('; '.join(env_vars_to_include)))

if len(args.exclude) > 0:
    env_vars_to_exclude = args.exclude.split(",")
    print('Excluding: {}'.format('; '.join(env_vars_to_exclude)))

client = boto3.client('ssm')

for key, value in env_values.items():
    if len(env_vars_to_include) > 0 and key not in env_vars_to_include:
        continue

    if key in env_vars_to_exclude:
        print('Skipping {}'.format(key))
        continue

    paramPath = '{}/{}'.format(args.paramStorePrefix, key)
    response = client.put_parameter(
        Name=paramPath,
        Value=value,
        Type='SecureString',
        Overwrite=True
    )
    # print(response)
    if response['ResponseMetadata']['HTTPStatusCode'] == 200:
        print('Wrote {}'.format(paramPath))
    else:
        print('Failed to write {}'.format(paramPath))

print('Done')
