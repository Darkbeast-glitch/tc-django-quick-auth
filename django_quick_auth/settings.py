# django_quick_auth/settings.py
from django.conf import settings
from datetime import timedelta

QUICK_AUTH = getattr(settings, 'QUICK_AUTH', {})
USE_JWT = QUICK_AUTH.get('USE_JWT', False)

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': QUICK_AUTH.get('ACCESS_TOKEN_LIFETIME', timedelta(minutes=60)),
    'REFRESH_TOKEN_LIFETIME': QUICK_AUTH.get('REFRESH_TOKEN_LIFETIME', timedelta(days=1)),
    'ROTATE_REFRESH_TOKENS': QUICK_AUTH.get('ROTATE_REFRESH_TOKENS', False),
    'BLACKLIST_AFTER_ROTATION': QUICK_AUTH.get('BLACKLIST_AFTER_ROTATION', False),
    'AUTH_HEADER_TYPES': ('Bearer',),
}