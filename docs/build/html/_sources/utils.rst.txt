Utility Functions
=================

File Detection
--------------

.. autofunction:: utils.decrypt_utils.detect_file_type

Supported Formats
----------------

.. list-table:: File Signatures
   :widths: 20 20 60
   :header-rows: 1

   * - Magic Bytes
     - Extension
     - File Type
   * - 50 4B 03 04
     - .xlsx
     - Excel/Office Open XML
   * - 25 50 44 46
     - .pdf
     - PDF Document
   * - 89 50 4E 47
     - .png
     - PNG Image
   * - FF D8 FF
     - .jpg
     - JPEG Image
   * - 42 4D
     - .bmp
     - Bitmap Image
   * - 7F 45 4C 46
     - .elf
     - Executable
   * - 52 61 72 21 1A 07 00
     - .rar
     - RAR Archive

Usage Example
------------

.. code-block:: python

   with open('unknown.bin', 'rb') as f:
       file_type = detect_file_type(f.read(8))
   print(f"File is of type: {file_type}")