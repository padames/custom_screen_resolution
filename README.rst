========================
Custom Screen Resolution
========================

.. image:: https://snapcraft.io//custom-screen-resolution/badge.svg
        :target: https://snapcraft.io/custom-screen-resolution

.. image:: https://img.shields.io/pypi/v/custom_screen_resolution.svg
        :target: https://pypi.python.org/pypi/custom_screen_resolution

.. image:: https://travis-ci.com/anopensourcecoder/custom_screen_resolution.svg?branch=master
        :target: https://travis-ci.com/anopensourcecoder/custom_screen_resolution

.. image:: https://readthedocs.org/projects/custom-screen-resolution/badge/?version=latest
        :target: https://custom-screen-resolution.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status


.. image:: https://pyup.io/repos/github/anopensourcecoder/custom_screen_resolution/shield.svg
     :target: https://pyup.io/repos/github/anopensourcecoder/custom_screen_resolution/
     :alt: Updates



Create custom resolution base on screen size, dpi and zoom level.

I find myself to be comfortable with screen DPI between 100 to 140.
It also depends to the distance between display and my eyes.
Plus the font size and sharpness of font.

High DPI might be usefull for graphic software
but it has issues with remote desktop and older software.
Also when you have multiple displays with different DPI.

This software allows you to find out the best DPI that can solve these problems.
It can also suggest the same DPI at higher scaling level.
For example a 14 inch display with resolution of 2560x1440 has a DPI equal to 209.

dpi 2560 1440 14
DPI:    209.80

A quick solution is to set the resolution to 1280x720 because the DPI of 100.5 falls into comfortable level.
dpi 1280 720 14
DPI:    104.90

Unfortunately, the output becomes blury because an LCD disply can only provide sharp images at native resolution.
This issue can be solved by creating a custom resolution that is integer scaled by 2.

Here is an example how you can calculate it:
2560 1440 14 --zoom 2
DPI:    104.90

As you see, we can have a lower DPI resolution at higer native LCD resolution that is integer scaled by 2.
This gives you the best of both worlds: sharp text with lower DPI.

Note: currently, only latest Xrandr development version hub support integer scaling.

This way you can have both sharp pixel at native resolution while having lower DPI.
You also can use it to have a lower resolution at your comfort DPI level.
This can help to save power and battery life that is important for portable devices.
Lower resolution and DPI consume lower internet bandwidth too.
This can improve remote desktop performance.



* Free software: GNU General Public License v3
* Documentation: https://custom-screen-resolution.readthedocs.io.


Features
--------

* Gui and Cli interface.
* Calculate Width and height base on screen size, dpi and aspect ratio
* Calculate screen size base on resolution and dpi
* Calculate screen size base on screen size and dpi and zoom level

How to install
--------------

.. image:: https://snapcraft.io/static/images/badges/en/snap-store-black.svg
        :target: https://snapcraft.io/custom-screen-resolution


Please install using Snapcraft::

    $ snap install custom-screen-resolution

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
