# setup.py
from setuptools import setup, find_packages
import os

# Validate README and LICENSE files
if not os.path.exists("README.md"):
    raise RuntimeError("README.md not found!")
if not os.path.exists("LICENSE"):
    raise RuntimeError("LICENSE file not found!")

setup(
    name="tc-django-quick-auth",
    version="0.1.2",
    author="Julius Boakye",
    author_email="juliusboakye@pythonghana.org",
    description="A reusable Django package for quick login and signup endpoints with optional JWT authentication",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Darkbeast-glitch/django-quick-auth",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "django>=3.2",
        "djangorestframework>=3.12",
        "djangorestframework-simplejwt>=5.2",
    ],
    keywords=["django", "authentication", "jwt", "login", "signup", "api"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Framework :: Django",
        "Framework :: Django :: 3.2",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.6",
)
