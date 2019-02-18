Path of Building API
====================

Pre-release Software Warning
----------------------------

| This library is currently in pre-release status and may change in the near future.
| Meanwhile I am looking forward to community feedback to accommodate most use cases.
| Pull requests are gladly accepted and much appreciated!

Introduction
------------

| Path Of Building API provides a comprehensive toolbox for processing
    `Path of Building <https://github.com/Openarl/PathOfBuilding>`_ pastebins.
| It is aimed at community developers:

* looking to add Path of Building functionality to their apps.
* upgrading from existing solutions.

| As PoB pastebins became the standard way to share theorycrafting and characters,
| community tools want to interact with them and users `increasingly expect such functionality
    <https://www.reddit.com/r/pathofexile/comments/aca7vl/path_of_leveling_a_tool_written_in_java_with_an/>`_.

Benefits from using this library:

* Focus on your app's core competences
* Spend your free time on unique features
* Backwards-compatibility as PoB's export format changes
* Tested and secure codebase

Features
--------

* Look up and process:
    * Character stats (DPS, life, etc.)
    * Skill trees
    * Skills, skill groups and links
    * Gear and item sets
    * Path of Building configuration settings
    * Build author's notes
* Exposes all of Path of Building's relevant stats and attributes in a simple and pythonic way.
* Low memory footprint through slots and dynamically generated attributes.
* Automatically calculates mod values on theorycrafted items.
* Secure against XML attacks thanks to the `defusedxml <https://pypi.org/project/defusedxml/>`_ library.

Requirements
------------

* `Python 3.7+ <https://www.python.org/>`_
* `defusedxml <https://pypi.org/project/defusedxml/>`_
* `lxml <https://pypi.org/project/lxml/>`_
* `requests <https://pypi.org/project/requests/>`_
* `unstdlib <https://pypi.org/project/unstdlib/>`_

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
>>> url = "https://pastebin.com/bQRjfedq"
>>> build = pobapi.from_url(url)
>>> print(build.ascendancy_name)
Elementalist
>>> print(build.bandit)
None
>>> print(build.stats.life)
6911.
>>> if "Blade Vortex" or "Vaal Blade Vortex" == build.active_skill.name:
...     if "Storm Brand" in build.skill_names:
...         print(build.config.brand_attached)
...
True
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

Documentation
-------------

Available at `Read the Docs <https://pobapi.readthedocs.io>`_.

Feedback
--------

Please file a `GitHub issue <https://developer.github.com/v3/issues/>`_ in this repository for any feedback you may have.

Contribution
------------

Pull requests are gladly accepted. Check out the `Developer Guide <https://pobapi.readthedocs.io/dev.html>`_.

To-Do
-----

* Support enchantments
* Support passive tree keystones

License
-------

`EUPL 1.2 <https://eupl.eu/>`_ (Think about it as an equivalent to LGPL + Affero clause).
