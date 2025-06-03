UMBRA Main Window
=================

.. automodule:: GUI.ui.main_window
   :members:
   :undoc-members:
   :show-inheritance:

UI Components
-------------

.. list-table:: Main Interface Elements
   :widths: 25 25 50
   :header-rows: 1

   * - Component
     - Type
     - Description
   * - Terminal
     - HackerTerminal
     - Primary output display
   * - Generate Button
     - QPushButton
     - Opens password generator
   * - Suggest Button
     - QPushButton
     - Opens password suggester
   * - Status Bar
     - QLabel
     - System status messages

Key Features
------------

- Animated boot sequence
- Typewriter text effects
- Module window management
- Consistent cyberpunk styling

Example Usage
-------------

.. code-block:: python

   from PyQt5.QtWidgets import QApplication
   from GUI.ui.main_window import UMRBAMainWindow

   app = QApplication([])
   window = UMRBAMainWindow()
   window.show()
   app.exec_()

See Also
--------

* :doc:`gui_generation` - Password generation module
* :doc:`gui_suggestion` - Password suggestion module