# How to Contribute

If you're interested in contributing, take a look at the general [contributor's guide](https://github.com/Microsoft/ApplicationInsights-Home/blob/master/CONTRIBUTING.md) first.

## Build

Run `python setup.py sdist`

## Test

- Unit tests: `python setup.py test`
- Django tests: `django_tests/all_tests.sh`

Use `pip install -e <path>` to install it into test application for the testing purposes.

## Releasing new version

This is for repository maintainers only:

This package is published to https://pypi.python.org/pypi/applicationinsights. These are the steps to publish the package.

1. Merge `develop` to `master` via [pull request](https://github.com/Microsoft/ApplicationInsights-Python/compare/master...develop).
2. Tag `master`. Use [CHANGELOG.md](CHANGELOG.md) to get release description.
3. Travis should release a new version. For manual steps:
    1. Clean up repo: `git clean -xfd`.
    2. Make sure `wheel` is installed: `sudo pip install wheel`.
    3. Make sure `twine` is installed: `sudo pip install twine`.
    4. Create distributions `python setup.py bdist_wheel`.
    5. Create `~/.pypirc` file with the following content
        ``` ini
        [distutils]
        index-servers=
        pypi

        [pypi]
        username:AppInsightsSDK
        password=<pwd here>
        ```
    6. Test distributive. You can upload it to https://test.pypi.org/ using `twine upload --repository-url https://test.pypi.org/legacy/ dist/*`
    7. Upload the package `twine upload dist/*`.
4. Update versions in `TelemetryChannel.py`, `CHANGELOG.md`, `conf.py` and `setup.py`.

## Contributing

This project welcomes contributions and suggestions. Most contributions require you to
agree to a Contributor License Agreement (CLA) declaring that you have the right to,
and actually do, grant us the rights to use your contribution. For details, visit
https://cla.microsoft.com.

When you submit a pull request, a CLA-bot will automatically determine whether you need
to provide a CLA and decorate the PR appropriately (e.g., label, comment). Simply follow the
instructions provided by the bot. You will only need to do this once across all repositories using our CLA.

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/)
or contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.