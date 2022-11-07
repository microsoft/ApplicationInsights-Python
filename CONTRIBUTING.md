# Azure Monitor Contributing Guide

This project welcomes contributions and suggestions. Most contributions require you to agree to a
Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us
the rights to use your contribution. For details, visit https://cla.opensource.microsoft.com.

When you submit a pull request, a CLA bot will automatically determine whether you need to provide
a CLA and decorate the PR appropriately (e.g., status check, comment). Simply follow the instructions
provided by the bot. You will only need to do this once across all repos using our CLA.

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or
contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.

## Reporting Bugs/Feature Requests

To report a bug or feature request, open up an [issue](https://github.com/microsoft/ApplicationInsights-Python/issues). Please provide as much information as possible. For example for a bug, describe your environment, provide steps to reproduce, expected behavior/actual behavior in the description.

## Contributing

Everyone is welcome to contribute code to this repository via GitHub
pull requests (PRs).

To create a new PR, fork the project in GitHub and clone the upstream repo:

```console
$ git clone https://github.com/microsoft/ApplicationInsights-Python.git
```

Add your fork as an origin:

```console
$ git remote add fork https://github.com/YOUR_GITHUB_USERNAME/microsoft/ApplicationInsights-python.git
```

Run tests:

```sh
# make sure you have all supported versions of Python installed
$ pip install tox  # only first time.
$ tox  # execute in the root of the repository
```

Check out a new branch, make modifications and push the branch to your fork:

```sh
$ git checkout -b feature
# edit files
$ git commit
$ git push fork feature
```

Open up a pull request with your changes.

## Development

This project uses [tox](https://tox.readthedocs.io) to automate
some aspects of development, including testing against multiple Python versions.
To install `tox`, run:

```console
$ pip install tox
```

We will use the Azure Monitor distro project as an example.
You can run `tox` with the following arguments:

- `tox` to run all existing tox commands, including unit tests for all packages
  under multiple Python versions
- `tox -e distro` to run the unit tests
- `tox -e py310-distro` to e.g. run the API unit tests under a specific
  Python version
- `tox -e spellcheck` to run a spellcheck on all the code
- `tox -e lint` to run lint checks on all code

`black` and `isort` are executed when `tox -e lint` is run. The reported errors can be tedious to fix manually.
An easier way to do so is:

1. Run `.tox/lint/bin/black .`
2. Run `.tox/lint/bin/isort .`

See
[`tox.ini`](https://github.com/microsoft/ApplicationInsights-Python/blob/main/tox.ini)
for more detail on available tox commands.

## Documentation

TODO

## Licensing

See the [LICENSE](LICENSE) file for our project's licensing. We will ask you to
confirm the licensing of your contribution.

## CLA

This project welcomes contributions and suggestions. Most contributions require you to
agree to a Contributor License Agreement (CLA) declaring that you have the right to,
and actually do, grant us the rights to use your contribution. For details, visit
https://cla.microsoft.com.

When you submit a pull request, a CLA-bot will automatically determine whether you need
to provide a CLA and decorate the PR appropriately (e.g., label, comment). Simply follow the
instructions provided by the bot. You will only need to do this once across all repositories using our CLA.

## Code of Conduct

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/)
or contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.
