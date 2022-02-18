import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="populate_ssm",
    version="0.2.1",
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
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    install_requires=["boto3==1.18.33", "python-dotenv==0.19.0"],
    setup_requires=["flake8"],
    entry_points={
        "console_scripts": [
            "populate-ssm = populate_ssm.__main__:main",
        ],
    },
)
