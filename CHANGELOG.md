# Changelog

## Unreleased (will be 0.11.8)

- Allow to specify and endpoint to upload telemetry to.
- Add support for using `NullSender` with `AsynchronousQueue`.

## 0.11.7

- Added `track_dependency`.
- Added optional `request_id` argument to `track_request`.

## 0.11.6

- Fixed exception logging in Flask integration on Python 2.
- Fixed setting attributes in channel through context
- Added support for Cloud Role Name and Cloud Role Instance fields 

## 0.11.5

- Fixed setting custom properties through context. [#102](https://github.com/Microsoft/ApplicationInsights-Python/pull/102)

## 0.11.4

- Schemas for all data types and context objects updated to the latest version.
- Add common properties argument to WSGIApplication initialization. Those common properties will be associated with telemetry produced by WSGIApplication.

## 0.11.3

- Changelog started from this version.
