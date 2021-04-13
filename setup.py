import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="populate-ssm",  # Replace with your own username
    version="0.1.0",
    author="Joe Niland",
    author_email="joe@deploymode.com",
    description="Populate AWS SSM Parameter Store from .env File",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/deploymode/populate-ssm",
    project_urls={
        "Bug Tracker": "https://github.com/deploymode/populate-ssm/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "populate_ssm"},
    packages=setuptools.find_packages(where="populate_ssm"),
    python_requires=">=3.6",
    install_requires=["boto3", "python-dotenv"],
    entry_points={
        "console_scripts": [
            "populate-ssm = populate_ssm.__main__:main",
        ],
    },
)