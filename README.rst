Path of Building API
====================

Pre-release Software Warning
----------------------------

This library is currently in pre-release status and may change in the future.
Meanwhile we are looking forward to community feedback to accommodate most use cases.

Introduction
------------

Path of Building API is an opinionated interface between
`Path of Building's <https://github.com/Openarl/PathOfBuilding>`_ import format and Python code.

Features
--------
* Look up and process:
    * Character stats (DPS, life, etc.)
    * Skill trees
    * Skills, skill groups and links
    * Gear and item sets
    * Path of Building configuration settings
    * Build author's notes
* Exposes (almost) all of Path of Building's stats and attributes in a simple and pythonic way.
* Low memory footprint through slots and dynamically generated attributes.
* Automatically calculates mod values on theorycrafted items.

Setup Instructions
--------------------

.. code-block:: console

    pip install pobapi

Setup Instructions For Developers
---------------------------------

Setup virtual environment:

.. code-block:: console

    pip install virtualenv
    cd my_project_folder
    virtualenv venv

To activate on Microsoft Windows:

.. code-block:: console

    \venv\Scripts\activate

To activate on GNU/Linux:

.. code-block:: console

    source venv/bin/activate

Setup repository:

.. code-block:: console

    git clone https://github.com/ppoelzl/PathOfBuildingAPI.git
    pip install -r requirements.txt

Basic Usage
-----------
>>> import pobapi
>>> with open("../resources/import_code.txt") as f:
...    code = f.read()
>>> build = pobapi.from_import_code(code)
>>> print(build.ascendancy_name)
Elementalist
>>> print(build.bandit)
None
>>> print(build.stats.life)
6911.0
>>> for item in build.items:
...    if item.name == "Inpulsa's Broken Heart":
...        print(item)
...        break
...
Rarity: Unique
Name: Inpulsa's Broken Heart
Base: Sadist Garb
Quality: 20
Sockets: (('G', 'G', 'G', 'B', 'B', 'B'),)
LevelReq: 68
ItemLvl: 71
+64 to maximum Life
26% increased Damage if you have Shocked an Enemy Recently
33% increased Effect of Shock
Shocked Enemies you Kill Explode, dealing 5% of
their Maximum Life as Lightning Damage which cannot Shock
Unaffected by Shock
>>> if "Blade Vortex" or "Vaal Blade Vortex" == build.active_skill.name:
...     if "Storm Brand" in build.skill_names:
...         print("Backup plan.")
...
Backup plan.

Documentation
-------------

Available at `Read the Docs <https://pobapi.readthedocs.io>`_.

Feedback
--------

Please file a `GitHub issue <https://developer.github.com/v3/issues/>`_ in this repository for any feedback you may have.

License
-------

`EUPL v1.2 <https://eupl.eu/>`_ (Think about it as an equivalent to LGPL + Affero Clause).
