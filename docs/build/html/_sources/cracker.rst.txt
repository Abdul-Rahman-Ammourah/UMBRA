Password Cracker
========================

.. automodule:: Cracker.Decrypter
   :members:
   :undoc-members:
   :show-inheritance:

File Format Specification
------------------------

Encrypted files must follow this exact structure:

.. list-table:: 
   :widths: 20 80
   :header-rows: 1

   * - Offset
     - Contents
   * - 0-15
     - 16-byte salt
   * - 16-31
     - 16-byte nonce
   * - 32-47
     - 16-byte authentication tag
   * - 48+
     - Encrypted payload

Cracking Process
---------------

.. mermaid::

   flowchart TD
       A[Start] --> B{Valid Input?}
       B -->|Yes| C[Load Wordlist]
       B -->|No| D[Error Exit]
       C --> E[Derive Key]
       E --> F[Decrypt+Verify]
       F -->|Success| G[Save File]
       F -->|Failure| H{More Passwords?}
       H -->|Yes| E
       H -->|No| I[Return Failure]

Security Notes
-------------

.. warning::
   - Always use strong passwords (12+ chars, mixed characters)
   - This implementation uses:
     - AES-256 in GCM mode
     - PBKDF2 with 1000 iterations
   - Brute-force protection is limited

Example Usage
------------

.. code-block:: text

   $ python main.py cracker
   [SYSTEM] AES-GCM Password Cracker Initialized
   Enter the path to the encrypted file: secret.doc.enc
   Available password lists:
   1. passwords1.txt
   2. passwords2.txt
   Select a password list by number: 1
   [INFO] Trying 1000 passwords...
   [✓] Password found: J@pan3seJazz1999
   [INFO] Detected file type: .docx
   [✓] Decrypted file saved as: secret_decrypted.docx

See Also
--------

* :doc:`password_gen` - For generating password wordlists
* :doc:`password_sug` - For creating targeted passwords