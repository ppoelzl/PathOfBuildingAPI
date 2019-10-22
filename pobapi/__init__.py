# Built-ins
import logging

# Project
from .api import *

VERSION = "0.3.1"
PROJECT = "Path Of Building API"
COPYRIGHT = "2019, Peter Pölzl"
AUTHOR = "Peter Pölzl"

logging.getLogger(__name__).addHandler(logging.NullHandler())
