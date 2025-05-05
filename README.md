# Django Quick Auth

[![PyPI version](https://img.shields.io/pypi/v/tc-django-quick-auth.svg)](https://pypi.org/project/tc-django-quick-auth/)
[![Python Versions](https://img.shields.io/pypi/pyversions/tc-django-quick-auth.svg)](https://pypi.org/project/tc-django-quick-auth/)
[![License](https://img.shields.io/pypi/l/tc-django-quick-auth.svg)](https://github.com/Darkbeast-glitch/django-quick-auth/blob/main/LICENSE)

A reusable Django package that provides quick and easy authentication endpoints for login and signup functionality with optional JWT authentication support. Simplify your Django project's authentication system without writing boilerplate code.

## Features

- Ready-to-use login and signup endpoints
- Optional JWT authentication support
- Customizable user model
- Easy integration with existing Django projects
- Fully configurable through settings

## Installation

```bash
pip install tc-django-quick-auth
```

> **Important Note**: While the package is installed as `tc-django-quick-auth`, you'll reference it in your Python code and Django settings as `django_quick_auth`. This follows Python package conventions where PyPI package names use hyphens, but Python module names use underscores.

## Configuration

### 1. Add to INSTALLED_APPS

Add `django_quick_auth` to your `INSTALLED_APPS` in your Django project's settings:

```python
INSTALLED_APPS = [
    # ...
    "rest_framework",
    "rest_framework_simplejwt",
    'django_quick_auth',
]
```

### 2. Configure User Model (Optional)

If you want to use the custom `QuickAuthUser` model provided by this package, add this to your settings:

```python
AUTH_USER_MODEL = 'django_quick_auth.QuickAuthUser'
```

**Note:** If you're adding this to an existing project that already has migrations with the default Django User model, you'll need to create a migration strategy or start with a fresh database.

### 3. URL Configuration

Include the authentication URLs in your project's `urls.py`:

```python
from django.urls import path, include

urlpatterns = [
    # ...
    path('api/auth/', include('django_quick_auth.urls')),
    # ...
]
```

### 4. JWT Configuration (Optional)

If you want to use JWT authentication, configure the JWT settings in your project settings:

```python
# JWT Settings
QUICK_AUTH = {
    'USE_JWT': True,
    'JWT_SECRET_KEY': 'your-secret-key',
    'JWT_ALGORITHM': 'HS256',
    'JWT_EXPIRATION_DELTA': 24 * 60 * 60,  # Token expiry time in seconds (24 hours)
    'JWT_REFRESH_EXPIRATION_DELTA': 7 * 24 * 60 * 60,  # Refresh token expiry time in seconds (7 days)
}
```

### 5. Run Migrations

After configuring your settings, run migrations to create the necessary database tables:

```bash
python manage.py makemigrations
python manage.py migrate
```

## Usage

### Authentication Endpoints

Once configured, the package provides the following endpoints:

- **POST /api/auth/signup/** - Register a new user

  ```json
  {
    "username": "newuser",
    "email": "user@example.com",
    "password": "securepassword"
  }
  ```

- **POST /api/auth/login/** - Login with existing credentials
  ```json
  {
    "username": "existinguser",
    "password": "securepassword"
  }
  ```

### JWT Authentication

If JWT is enabled, successful login/signup will return:

```json
{
  "token": "your.jwt.token",
  "refresh_token": "your.refresh.token",
  "user": {
    "id": 1,
    "username": "username",
    "email": "user@example.com"
  }
}
```

## Customization

### Custom User Fields

You can extend the `QuickAuthUser` model by creating your own model that inherits from it:

```python
from django_quick_auth.models import QuickAuthUser
from django.db import models

class MyCustomUser(QuickAuthUser):
    phone_number = models.CharField(max_length=15, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)

    # Don't forget to update AUTH_USER_MODEL in settings to point to your custom model
```

### Custom Serializers

You can override the default serializers by specifying them in your settings:

```python
QUICK_AUTH = {
    # Other settings...
    'USER_SERIALIZER': 'myapp.serializers.MyCustomUserSerializer',
    'LOGIN_SERIALIZER': 'myapp.serializers.MyCustomLoginSerializer',
    'SIGNUP_SERIALIZER': 'myapp.serializers.MyCustomSignupSerializer',
}
```

## Testing

To run the tests for this package:

```bash
pip install -e .
pip install pytest pytest-django
pytest
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -am 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
