.. UMBRA documentation master file, created by
   sphinx-quickstart on Tue Jun  3 02:37:34 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to UMBRA's Documentation!
=================================

**UMBRA** (User-tailored Model-Based Resourceful Algorithm) is a command-line cybersecurity tool developed for professionals and researchers. It leverages AI-powered password generation and analysis to provide secure password suggestions and simulate targeted password cracking attempts. 

While UMBRA was initially designed to incorporate OSINT techniques, this feature was removed due to practical limitations. The tool operates via a terminal interface, with an optional graphical user interface (GUI) that enhances usability and engagement.

This documentation will guide you through UMBRA's modules, features, and internal structure. It is written using ``reStructuredText`` and built with Sphinx.

For help with formatting or extending documentation, visit the
`reStructuredText guide <https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html>`_.
Contents
--------

.. toctree::
   :maxdepth: 2
   :caption: Modules:

   main
   password_sug
   password_gen
   cracker
   gui_generation
   gui_main
   gui_suggestion
   utils
   Backend

Indices and tables
==================

* :ref:`search`
