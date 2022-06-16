Populate AWS SSM Parameter Store from .env or .json files
=================================================

## Prerequisites

* Python3
* virtualenv

### Recommended

* aws-vault or leapp-cli

## Set up

### Dev install

```shell
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Local install (for usage)

To install a script in `/usr/local/bin/populate-ssm`:

```shell
pip3 install .
```

### Install from git

```shell
virtualenv venv
source venv/bin/activate
python -m pip install -e "git+https://github.com/deploymode/populate-ssm.git/#egg=populate-ssm"
```

## Testing

ave om-staging-admin -- python src/populate_ssm/__main__.py test/one.env /myorg/test/app


## Usage Example

```shell
export STAGE=staging
ave myorg-$STAGE-admin -- python __init__.py ../../../my-project/$STAGE.env /myorg/$STAGE/app
```