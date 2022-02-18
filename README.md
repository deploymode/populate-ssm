Populate AWS SSM Parameter Store from .env File
=================================================

## Prerequisites

* Python3
* virtualenv
* aws-vault

## Set up

### Local install

```shell
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
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