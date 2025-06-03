Password Suggestion GUI
=========================

.. automodule:: GUI.ui.sug_window
   :members:
   :undoc-members:
   :show-inheritance:

Input Fields
------------

.. list-table:: 
   :widths: 20 30 50
   :header-rows: 1

   * - Label
     - Key
     - Example
   * - Username
     - username
     - john_doe
   * - Birthdate
     - birthdate
     - 19900115
   * - Favorite thing
     - favorite_thing
     - StarWars
   * - Color
     - color
     - Blue
   * - Food
     - food
     - Pizza
   * - Animal
     - animal
     - Cat

Password Templates
------------------

1. FavoriteThing + day + symbol + color + Z
2. Animal + _ + month + symbol + food + 8  
3. Username + @ + color + symbol + year
4. Food + _ + year + ! + random
5. Animal + Luv + symbol + birthdate
6. Favorite + symbol + 4 + color + _ + month
7. Food + Crave + day + symbol
8. Username + symbol + Fav + birthdate + animal

Security Features
----------------

- Leetspeak substitutions (random 50% chance)
- Mandatory symbol insertion
- Mixed case enforcement
- Personal data fragmentation
- Minimum 12 character length

Example Output
-------------

.. code-block:: text

   1. M0v13$0421BlZ
   2. C@t_08!Pi8  
   3. Joh@Blue$22
   4. P1zza_2023!45
   5. D0gLuv^1995
   6. M@tr1x$4Blu_07
   7. P1zzaCr@ve15%
   8. J0hn$Fav95D

See Also
--------

* :doc:`gui_main` - Main application window
* :doc:`gui_generation` - AI password generation