User Guide
==========

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

Using this library
------------------

The library is divided into roughly 4 components:

* Main interface (api.py)
* Dataclass templates (models.py, config.py, stats.py)
* Internals (util.py)
* Data (constants.py)

| All user interaction is handled through the main interface.
| However, when in doubt of the type or format of a stat, have a look at the dataclass templates.

Full documentation available :ref:`here <api:API>`.

.. note:: Internals are subject to continued maintenance and unannounced changes.
