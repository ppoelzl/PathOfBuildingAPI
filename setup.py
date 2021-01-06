# Always prefer setuptools over distutils
import sys
from os import path

from setuptools import setup

sys.path.insert(0, path.abspath('..'))

import pobapi

here = path.abspath(path.dirname(__file__))

# Get the long description from the relevant file
with open(path.join(here, "README.rst"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="pobapi",
    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # http://packaging.python.org/en/latest/tutorial.html#version
    version=pobapi.VERSION,
    description="API for Path Of Building's build sharing format.",
    long_description=long_description,
    # The project's main homepage.
    url="https://github.com/ppoelzl/PathOfBuildingAPI",
    # Author details
    author=pobapi.AUTHOR,
    author_email="",
    # Choose your license
    license="MIT",
    # See https://PyPI.python.org/PyPI?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        "Development Status :: 4 - Beta",
        # Indicate who your project is intended for
        "Intended Audience :: Developers",
        "Topic :: Documentation :: Sphinx",
        "Topic :: Games/Entertainment",
        "Topic :: Software Development :: Libraries",
        "Topic :: Text Processing :: Markup :: XML",
        # Pick your license as you wish (should match "license" above)
        "License :: OSI Approved :: MIT License",
        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    # What does your project relate to?
    keywords="pathofexile poe pathofbuilding pob",
    packages=["pobapi"],
    install_requires=["dataslots", "lxml", "requests", "unstdlib"],
)
