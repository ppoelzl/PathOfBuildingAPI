from setuptools import setup

setup(
   name='pobapi',
   version='0.1.0',
   description="An API for Path Of Building's build export format.",
   author="Peter Pölzl",
   author_email="peter.poelzl@mailbox.org",
   packages=['pobapi'],
   install_requires=["defusedxml", "lxml", "requests"],
)
