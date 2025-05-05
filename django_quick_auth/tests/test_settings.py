# tests/test_settings.py
INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",  # Add this
    "rest_framework",
    "rest_framework_simplejwt",
    "django_quick_auth",
    "tests",
]

MIDDLEWARE = [
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}

ROOT_URLCONF = "tests.urls"  # Add this line

SECRET_KEY = "test-secret-key"
AUTH_USER_MODEL = "auth.User"  # Use the default User model for testing

# Configure authentication backends
AUTHENTICATION_BACKENDS = [
    "django_quick_auth.authentication.EmailBackend",  # Custom backend that handles email auth
    "django.contrib.auth.backends.ModelBackend",  # Default backend
]

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.AllowAny",
    ],
}

# JWT settings
SIMPLE_JWT = {
    "AUTH_HEADER_TYPES": ("Bearer",),
    "USER_ID_FIELD": "id",
    "USER_ID_CLAIM": "user_id",
}

# Quick Auth settings
QUICK_AUTH = {
    "USE_JWT": False,  # Default to session authentication
    "LOGIN_FIELD": "email",
}
