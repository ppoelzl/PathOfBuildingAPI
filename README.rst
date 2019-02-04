Path of Building API
====================

Pre-release Software Warning
----------------------------

This library is currently in pre-release status and may change in the future.
Meanwhile we are looking forward to community feedback to accommodate most use cases.

Introduction
------------

Path of Building API is an opinionated interface between Path of Building's import format and Python code.

Setup instructions
------------------

``pip install pobapi``

Setup instructions for developers
---------------------------------
``pip install virtualenv``
``cd my_project_folder``
``virtualenv venv``
To activate on Windows:
``\venv\Scripts\activate``
``git clone https://github.com/ppoelzl/PathOfBuildingAPI.git``
``pip install -r requirements.txt``

Basic usage
-----------

``>>>import pobapi``

``>>>build = pobapi.from_url(URL)``

``>>>print(build.ascendancy)``
``Elementalist``

``>>>print(build.bandit)``
``Alira``

``>>>for item in build.items:``
``>>>  if item.name == "Inpulsa's Broken Heart":``
``>>>        print(item)``
``Rarity: Unique``
``Name: Inpulsa's Broken Heart``
``Base: Sadist Garb``
``Quality: 20``
``Sockets: (("B", "B", "G", "G", "G", "B"))``
``LevelReq: 68``
``ItemLvl: 80``
``Implicits: 0``
``+70 to maximum Life``
``35% increased Damage if you have Shocked an Enemy Recently``
``33% increased Effect of Shock``
``Unaffected by Shock``
``Shocked Enemies you Kill Explode, dealing 5% of``
``their Maximum Life as Lightning Damage which cannot Shock``

``>>>if "Arc" == build.active_skill.name and "Storm Brand" in build.skill_names:``
``>>>    print("Backup plan.")``
``Backup plan.``

``>>>print(build.stats.life):``
``6800``

Documentation
-------------

Available at `Read the Docs <https://pobapi.readthedocs.io>`_.

Feedback
--------

Please file a GitHub issue in this repository for any feedback you may have.

License
-------

`EUPL v1.2 <https://eupl.eu/>`_ (Think about it as an equivalent to LGPL + Affero Clause).
