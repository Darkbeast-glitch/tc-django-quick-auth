# django_quick_auth/models.py
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class QuickAuthUser(AbstractUser):
    email = models.EmailField(unique=True)

    # Override groups and user_permissions with custom related_name
    groups = models.ManyToManyField(
        Group,
        verbose_name="groups",
        blank=True,
        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
        related_name="quickauthuser_set",
        related_query_name="user",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name="user permissions",
        blank=True,
        help_text="Specific permissions for this user.",
        related_name="quickauthuser_set",
        related_query_name="user",
    )

    def __str__(self):
        return self.username
