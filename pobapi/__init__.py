# Built-ins
import logging

# Project
from .api import *

VERSION = "0.2.6"
PROJECT = "Path Of Building API"
COPYRIGHT = "2019, Peter Pölzl"
AUTHOR = "Peter Pölzl"

logging.getLogger(__name__).addHandler(logging.NullHandler())
