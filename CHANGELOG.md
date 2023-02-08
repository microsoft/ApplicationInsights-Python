# Changelog

## Unreleased

- Made build.sh script executible from publish workflow
    ([#213](https://github.com/microsoft/ApplicationInsights-Python/pull/213))
- Updated main and distro READMEs
    ([#205](https://github.com/microsoft/ApplicationInsights-Python/pull/205))
- Update CONTRIBUTING.md, support Py3.11
    ([#210](https://github.com/microsoft/ApplicationInsights-Python/pull/210))
- Added Diagnostic Logging for App Service
    ([#212](https://github.com/microsoft/ApplicationInsights-Python/pull/212))
- Updated setup.py, directory structure
    ([#214](https://github.com/microsoft/ApplicationInsights-Python/pull/214))
- Introduce Distro API
    ([#215](https://github.com/microsoft/ApplicationInsights-Python/pull/215))
- Rename to `configure_azure_monitor`, add sampler to config
    ([#216](https://github.com/microsoft/ApplicationInsights-Python/pull/216))
- Added Status Logger
    ([#217](https://github.com/microsoft/ApplicationInsights-Python/pull/217))
- Add Logging configuration to Distro API
    ([#218](https://github.com/microsoft/ApplicationInsights-Python/pull/218))
- Add instrumentation selection config
    ([#228](https://github.com/microsoft/ApplicationInsights-Python/pull/228))
- Removing diagnostic logging from its module's logger.
    ([#225](https://github.com/microsoft/ApplicationInsights-Python/pull/225))
- Add ability to specify logger for logging configuration
    ([#227](https://github.com/microsoft/ApplicationInsights-Python/pull/227))
- Add metric configuration to distro api
    ([#232](https://github.com/microsoft/ApplicationInsights-Python/pull/232))
- Add ability to pass custom configuration into instrumentations
    ([#235](https://github.com/microsoft/ApplicationInsights-Python/pull/235))
- Fix export interval bug
    ([#237](https://github.com/microsoft/ApplicationInsights-Python/pull/237))
- Add ability to specify custom span processors and metric readers
    ([#237](https://github.com/microsoft/ApplicationInsights-Python/pull/237))

## [1.0.0b8](https://github.com/microsoft/ApplicationInsights-Python/releases/tag/v1.0.0b8) - 2022-09-26

- Changing instrumentation dependencies to ~=0.33b0
    ([#203](https://github.com/microsoft/ApplicationInsights-Python/pull/203))

## [1.0.0b7](https://github.com/microsoft/ApplicationInsights-Python/releases/tag/v1.0.0b7) - 2022-09-26

- Moved and updated README
    ([#201](https://github.com/microsoft/ApplicationInsights-Python/pull/201))
- Adding requests, flask, and psycopg2 instrumentations
    ([#199](https://github.com/microsoft/ApplicationInsights-Python/pull/199))
- Added publishing action
    ([#193](https://github.com/microsoft/ApplicationInsights-Python/pull/193))

## [1.0.0b6](https://github.com/microsoft/ApplicationInsights-Python/releases/tag/v1.0.0b6) - 2022-08-30

- Drop support for Python 3.6
    ([#190](https://github.com/microsoft/ApplicationInsights-Python/pull/190))
- Changed repository structure to use submodules
    ([#190](https://github.com/microsoft/ApplicationInsights-Python/pull/190))
- Added OpenTelemetry Distro and Configurator
    ([#187](https://github.com/microsoft/ApplicationInsights-Python/pull/187))
- Initial commit
