# Built-ins
import logging

# Project
from .api import *

VERSION = "0.6.0"
PROJECT = "Path Of Building API"
COPYRIGHT = "2020, Peter Pölzl"
AUTHOR = "Peter Pölzl"

logging.getLogger(__name__).addHandler(logging.NullHandler())
