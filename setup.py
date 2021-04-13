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
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)