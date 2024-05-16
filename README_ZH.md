# 快速 pylib

[![自动 CI 和构建工具](https://github.com/aboutmydreams/quick-pylib/actions/workflows/ci-test.yml/badge.svg)](https://github.com/aboutmydreams/quick-pylib/actions/workflows/ci-test.yml)
[![自动发布到 PyPI 和 GitHub 发布](https://github.com/aboutmydreams/quick-pylib/actions/workflows/release.yml/badge.svg)](https://github.com/aboutmydreams/quick-pylib/actions/workflows/release.yml)
[![发布版本](https://img.shields.io/github/release/aboutmydreams/quick-pylib.svg)](https://github.com/aboutmydreams/quick-pylib/releases)
[![访问量](https://komarev.com/ghpvc/?username=aboutmydreams&repo=quick-pylib)](https://github.com/aboutmydreams/quick-pylib)
[![许可证](https://img.shields.io/github/license/aboutmydreams/quick-pylib.svg)](https://github.com/aboutmydreams/quick-pylib/license)
[![星标](https://img.shields.io/github/stars/aboutmydreams/quick-pylib.svg)](https://github.com/aboutmydreams/quick-pylib/stargazers)
[![分支](https://img.shields.io/github/forks/aboutmydreams/quick-pylib.svg)](https://github.com/aboutmydreams/quick-pylib/network)
[![下载量](https://pepy.tech/badge/quick-pylib)](https://pepy.tech/project/quick-pylib)
[![贡献者](https://img.shields.io/github/contributors/aboutmydreams/quick-pylib.svg)](https://github.com/aboutmydreams/quick-pylib/graphs/contributors)

一个快速发布且易于维护的 Python 库开发模板。

## 快速开始

- 将所有 `example_lib_name` 修改为 `your_lib_name`
- 编辑 `hello_world.py`（这是你的库的主要代码），并记得修改文件名 😊
- 选择库许可证。[Choosealicense] 网站会很有帮助。
- 编写自己的代码、文档和测试。
- 修改 `setup.py` 中此库的描述。

## 手动发布

- `python3 setup.py sdist bdist_wheel`（如果你没有安装 setuptools 和 wheel，请运行 `pip3 install setuptools wheel`）

- `twine upload dist/*`（如果你没有安装 twine，请运行 `pip3 install twine`）

- 在命令行中输入你的 API 令牌，如果你没有 API 令牌

### 通过一个命令手动运行脚本

`python3 update_version.py; git add -A; git commit -m"update version name"; git push; python3 setup.py sdist bdist_wheel; twine upload dist/*`

### PreCommit 设置（如果你想自动更新版本）

在终端中，输入 vim `.git/hooks/pre-commit` 打开 pre-commit 钩子脚本。将以下行添加到文件中：#!/bin/bash

```bash
# 在提交之前运行 update_version.py 脚本。
python3 update_version.py

# 继续提交。
git add -A
```

确保脚本具有执行权限：
`chmod +x .git/hooks/pre-commit`

这段代码设置了一个 Git 钩子，在每次提交之前运行 update_version.py 脚本。此脚本会更新 Python 包的 setup.py 文件中的版本号。该钩子还会自动将更改提交到 setup.py 文件中。这样可以确保版本号始终是最新的，并且更改包含在提交中。

## 使用 GitHub Action

此操作支持 PyPI 的[受信任发布]实现，允许在不手动配置 API 令牌或用户名/密码组合的情况下对 PyPI 进行身份验证。要使用此操作执行[受信任发布]，您的项目的发布者必须已经在[PyPI 上配置]。

在此示例中，在您的存储库设置中添加您的 [PYPI_API_TOKEN] 和 [RESP_GITHUB_TOKEN]：`https://github.com/your_github_name/your_lib_name/settings/secrets/actions`

## 运行测试

- 将 `test_hello_world.py` 更改为测试您的库函数。
- 运行 `python3 -m unittest discover -s tests`

## 令牌安全性

我建议您第一次使用手动发布，并在后续发布中选择操作发布。因为只有在您手动发布后，才能有选择性地获取仅对此库有效的令牌，这样使用此令牌进行操作会更安全。

[受信任发布]: https://docs.pypi.org/trusted-publishers/
[PyPI 上配置]: https://docs.pypi.org/trusted-publishers/adding-a-publisher/
[PYPI_API_TOKEN]: https://pypi.org/help/#apitoken
[RESP_GITHUB_TOKEN]: https://github.com/settings/tokens?type=beta
[Choosealicense]: https://choosealicense.com
