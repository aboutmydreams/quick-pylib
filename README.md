# quick-pylib

A python library development template that is quick to release and easy to maintain.

## Quick starter

- Change all `example_lib_name` to `your_lib_name`
- Edit `hello_world.py` (that's your library main code), and remenber to change the file name 😊
- Select the library license. [Choosealicense] website will be helpful.

## Publish manually

- `python3 setup.py sdist bdist_wheel` (if you not have setuptools and wheel, run `pip3 install setuptools wheel`)

- `twine upload dist/*`  (if you not have twine, run `pip3 install twine`)

- input the your API token in cmd, if you not have a api token

### Run the script manually by one command

`python3 update_version.py; git add -A; git commit -m"update version name"; git push; python3 setup.py sdist bdist_wheel; twine upload dist/*`

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

