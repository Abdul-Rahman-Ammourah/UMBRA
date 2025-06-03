Password Generation GUI
=======================

.. automodule:: GUI.ui.generation_window
   :members:
   :undoc-members:
   :show-inheritance:

UI Components
-------------

.. list-table:: Interface Elements
   :widths: 20 30 50
   :header-rows: 1

   * - Widget
     - Type
     - Purpose
   * - Terminal
     - QTextEdit
     - Displays generation output
   * - Name Field
     - QLineEdit
     - Target username
   * - Birthdate
     - QLineEdit
     - Birth year (YYYY)
   * - Hobbies
     - QLineEdit
     - Interests/activities
   * - Favorite
     - QLineEdit
     - Favorite items
   * - Generate
     - QPushButton
     - Initiate process

Workflow
--------

.. mermaid::

   sequenceDiagram
       User->>+GUI: Enters profile data
       GUI->>+Core: Passes parameters
       Core->>+AI: Generates passwords
       AI-->>-Core: Returns results
       Core-->>-GUI: Passes back
       GUI->>+Filesystem: Saves output
       GUI-->>-User: Shows completion

Styling
-------

Color Scheme:

.. list-table::
   :widths: 20 30 50
   :header-rows: 1

   * - Element
     - Hex Code
     - Usage
   * - Background
     - #121212
     - Main window
   * - Text
     - #00ff00
     - Primary text
   * - Accent
     - #005500
     - Borders
   * - Console
     - #0a0a0a
     - Terminal BG

Example Usage
------------

.. code-block:: python

   from GUI.ui.generation_window import GenerationWindow
   from PyQt5.QtWidgets import QApplication

   app = QApplication([])
   window = GenerationWindow()
   window.exec_()

See Also
--------

* :doc:`password_gen` - Core generation logic
* :doc:`gui_main` - Main application window