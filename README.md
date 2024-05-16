# quick-pylib

[![Auto CI and Build Tools](https://github.com/aboutmydreams/quick-pylib/actions/workflows/ci-test.yml/badge.svg)](https://github.com/aboutmydreams/quick-pylib/actions/workflows/ci-test.yml)
[![Auto Publish to PyPI and GitHub Release](https://github.com/aboutmydreams/quick-pylib/actions/workflows/release.yml/badge.svg)](https://github.com/aboutmydreams/quick-pylib/actions/workflows/release.yml)
[![Release Version](https://img.shields.io/github/release/aboutmydreams/quick-pylib.svg)](https://github.com/aboutmydreams/quick-pylib/releases)
[![Visits](https://komarev.com/ghpvc/?username=aboutmydreams&repo=quick-pylib)](https://github.com/aboutmydreams/quick-pylib)
[![License](https://img.shields.io/github/license/aboutmydreams/quick-pylib.svg)](https://github.com/aboutmydreams/quick-pylib/license)
[![Stars](https://img.shields.io/github/stars/aboutmydreams/quick-pylib.svg)](https://github.com/aboutmydreams/quick-pylib/stargazers)
[![Forks](https://img.shields.io/github/forks/aboutmydreams/quick-pylib.svg)](https://github.com/aboutmydreams/quick-pylib/network)
[![Downloads](https://pepy.tech/badge/quick-pylib)](https://pepy.tech/project/quick-pylib)
[![Contributors](https://img.shields.io/github/contributors/aboutmydreams/quick-pylib.svg)](https://github.com/aboutmydreams/quick-pylib/graphs/contributors)

A python library development template that is quick to release and easy to maintain.

## Quick starter

- Modify all `example_lib_name` to `your_lib_name`
- Edit `hello_world.py` (that's your library main code), and remenber to modify the file name 😊
- Select the library license. [Choosealicense] website will be helpful.
- Write your own code, documentation and test.
- Modify the description of this library in `setup.py`

## Publish manually

- `python3 setup.py sdist bdist_wheel` (if you not have setuptools and wheel, run `pip3 install setuptools wheel`)

- `twine upload dist/*`  (if you not have twine, run `pip3 install twine`)

- input the your API token in cmd, if you not have a api token

### Run the script manually by one command

`python3 update_version.py; git add -A; git commit -m"update version name"; git push; python3 setup.py sdist bdist_wheel; twine upload dist/*`

### PreCommit setting(If you want to automatically update version)

In the terminal, enter vim `.git/hooks/pre-commit` to open the pre-commit hook script. Add the following lines to the file: #!/bin/bash

```bash
# Run the update_version.py script before committing.
python3 update_version.py

# Continue with the commit.
git add -A
```

Ensure that the script has execute permissions: 
`chmod +x .git/hooks/pre-commit`

This code sets up a Git hook that runs the update_version.py script before each commit. This script updates the version number in your Python package’s setup.py file. The hook also automatically stages the changes to the setup.py file. This ensures that the version number is always up-to-date and that the changes are included in the commit.

## Use github action

This action supports PyPI's [trusted publishing]
implementation, which allows authentication to PyPI without a manually
configured API token or username/password combination. To perform
[trusted publishing] with this action, your project's
publisher must already be [configured on PyPI].

In this example case, add your [PYPI_API_TOKEN] and [RESP_GITHUB_TOKEN] in your repository setting: `https://github.com/your_github_name/your_lib_name/settings/secrets/actions`

## Run test

- Change the `test_hello_world.py` to test your library functions.
- Run `python3 -m unittest discover -s tests`

## Token security

I recommend that you use manual publishing for the first time, and choose action publishing in subsequent releases. Because only after you publish manually can you selectively obtain the token that is only valid for this library, it will be safer to use this token for action.

[trusted publishing]: https://docs.pypi.org/trusted-publishers/
[configured on PyPI]: https://docs.pypi.org/trusted-publishers/adding-a-publisher/
[PYPI_API_TOKEN]: https://pypi.org/help/#apitoken
[RESP_GITHUB_TOKEN]: https://github.com/settings/tokens?type=beta
[Choosealicense]: https://choosealicense.com
