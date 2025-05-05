# Changelog

All notable changes to the tc-django-quick-auth package will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.1] - 2023-05-05

### Fixed
- Added proper related_name attributes to QuickAuthUser model to prevent clashes with Django's default User model
- Updated README with clearer installation and usage instructions

## [0.1.0] - 2023-05-04

### Added
- Initial release of tc-django-quick-auth
- Basic authentication endpoints for login and signup
- JWT authentication support
- Custom user model
- Email-based authentication backend