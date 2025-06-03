Main
===========

.. automodule:: main
   :members:
   :undoc-members:
   :show-inheritance:
   :special-members: __init__

Command Line Interface
---------------------

The interactive mode provides these commands:

.. list-table:: Available Commands
   :widths: 20 80
   :header-rows: 1

   * - Command
     - Description
   * - generate/gen/g
     - Generate secure passwords
   * - gui/menu/m
     - Launch graphical interface
   * - suggest/s/sug
     - Get password suggestions
   * - cracker/crack/c
     - Run password cracking tool
   * - exit/quit/q/e/x
     - Quit the program

Example Usage
------------

.. code-block:: python

    # From command line:
    python main.py
    
    # Then type commands like:
    [UMBRA] >> generate
    [UMBRA] >> gui

See Also
--------

* :doc:`password_gen` - Password generation documentation
* :doc:`password_sug` - Password suggestion documentation
* :doc:`cracker` - Password cracking documentation