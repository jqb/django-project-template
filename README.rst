Django project directory layout.
================================

This is Django project directory layout which I use.

Included:
---------

- sample Fabric fabfile.py to make deployment painless,
- basic project  templates, with jquery, jquery-ui  included.  You can
  change jquery-ui theme and version of those libraries in settings.py
  file.

::

    # ...
    JQUERY_VER = '1.4.3'
    JQUERY_UI_VER = '1.8.5'
    JQUERY_UI_THEME = 'ui-lightness'
    # JQUERY UI PROVIDES FOLLOWING THEMES:
    # base, black-tie, blitzer, cupertino, dark-hive, dot-luv,
    # eggplant, excite-bike, flick, hot-sneaks, humanity,
    # le-frog, mint-choc, overcast, pepper-grinder, redmond,
    # smoothness, south-street, start, sunny, swanky-purse,
    # trontastic, ui-darkness, ui-lightness, vader


- django-debug-toolbar included,
- basic configuration for developement with sqlite3



Concepts:
---------

- project's (django) applications are in ./project/apps/ directory.
  (git doesn't allow to keep empty directories so you have to create it by hand)
- it uses jquery at google's ajax: googleapis.com so keep it in mind that
  javaScript won't work without internet connection.



Usage:
------

1) clone the repository:::

   $ git clone https://jqb@github.com/jqb/django-project-template.git

2) remove version control directory:::

   $ rm -rf django-project-template/.git

3) rename the project directory::

   $ mv django-project-template my-cool-project

4) It should work:::

   $ cd my-cool-project/project/ && ./manage.py runserver

5) Don't forget to change this README file :)
