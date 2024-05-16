import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="example_lib_name",
    version="0.0.1",
    author="your_github_name",
    author_email="author_email",
    description="your_lib_description",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="your_github_url",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache License",
        "Operating System :: OS Independent",
    ],
)
