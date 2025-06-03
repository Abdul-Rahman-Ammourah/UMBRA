Password Suggestion
=========================

.. automodule:: password_sug.password_sug
   :members:
   :undoc-members:
   :show-inheritance:

Algorithm Details
----------------

The password suggestion algorithm:

1. Collects these personal details:
   - Username
   - Birthdate (YYYYMMDD format)
   - Favorite things (movie, car, etc.)
   - Favorite color
   - Favorite food
   - Favorite animal

2. Applies these security transformations:
   - :func:`capitalize_mix`: Proper case mixing
   - :func:`to_leet`: Strategic leetspeak substitutions
   - :func:`rand_symbol`: Random symbol insertion
   - Length enforcement (minimum 12 chars)
   - Number incorporation

Example Output
-------------

Typical generated passwords look like:

.. code-block:: text

    1. M0v13$0421BlZ
    2. C@t_08!Pi8
    3. Joh@Blue$22
    4. P1zza_2023!45
    5. D0gLuv^1995
    6. M@tr1x$4Blu_07
    7. P1zzaCr@ve15%
    8. J0hn$Fav95D

Security Guarantees
------------------

All passwords meet these standards:

.. list-table:: 
   :widths: 30 70
   :header-rows: 1

   * - Requirement
     - Implementation
   * - Length
     - Minimum 12 characters
   * - Complexity
     - Upper + lowercase + digits + symbols
   * - Unpredictability
     - Random element combinations
   * - Memorability
     - Based on personal information
   * - Leak Resistance
     - Not directly using full personal data

See Also
--------

* :doc:`../password_gen` - For random password generation
* :doc:`../cracker` - For password strength testing