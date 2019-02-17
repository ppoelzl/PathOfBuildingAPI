User Guide
**********

Introduction
------------

| At it's core, Path Of Building API provides a single API object instantiated from an import code.
| All of it's functions are parameter-less and accessed as attributes.
| API objects are very space efficient, as attributes are only calculated on first access and then stored for later use.

.. note:: Attributes in plural (e.g. items) are always iterable, while attributes containing "active" never are.

Design Choices
--------------

| There is only a thin abstraction layer on top of  PoB's internal organisation.
| This is deliberate to ensure easy adoption and development.
| The focus is more on getting the data in the right format, so it feels native to Python.

Getting Started
---------------

| Create a new API object with :func:`pobapi.api.from_url` or :func:`pobapi.api.from_import_code`.
| Access PoB build information through attributes of the object.

Full documentation available :ref:`here <api:API>`.
