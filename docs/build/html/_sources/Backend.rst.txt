Password Generator API
=======================

.. automodule:: Backend.password_gen
   :members:
   :undoc-members:
   :show-inheritance:

API Endpoint
------------

**POST** `/generate-passwords`

Generates targeted password suggestions based on personal details using a fine-tuned GPT-2 language model.

Request Format
^^^^^^^^^^^^^^

Send a JSON payload with the following fields:

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - Field
     - Description
   * - ``Uname``
     - Required. User's name.
   * - ``Byear``
     - Required. Birth year (string or number).
   * - ``Fav``
     - Required. Favorite item or keyword.
   * - ``City``
     - Required. City name.
   * - ``Hobby``
     - Required. User's hobby or interest.
   * - ``Chunksize``
     - Optional. Number of generation attempts (default: 100).

Example Input:

.. code-block:: json

   {
     "Uname": "Alice",
     "Byear": "1988",
     "Fav": "Soccer",
     "City": "Paris",
     "Hobby": "Drawing",
     "Chunksize": 50
   }

Response Format
^^^^^^^^^^^^^^^

Returns a JSON object containing:

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - Field
     - Description
   * - ``results``
     - List of generated passwords (strings).
   * - ``time_taken_seconds``
     - Time taken for generation, in seconds.

Example Response:

.. code-block:: json

   {
     "results": ["AliceDraw88", "ParisSoccer1", "Dra1988Par"],
     "time_taken_seconds": 2.31
   }

Model Configuration
-------------------

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Parameter
     - Value
   * - Model
     - GPT-2 (fine-tuned, local path `Backend\GPT2`)
   * - Tokenizer
     - GPT-2 base
   * - max_new_tokens
     - 10
   * - top_k
     - 50
   * - top_p
     - 0.96
   * - temperature
     - 0.65
   * - num_return_sequences
     - 3
   * - device
     - CUDA (if available), otherwise CPU

Security Considerations
------------------------

.. warning::
   - Generated passwords may resemble personal info — use only for internal testing.
   - Avoid using these suggestions directly as actual secure passwords.
   - This tool is meant for password **cracking simulations** and **targeted password list generation** for ethical security assessments only.

Example Usage
-------------

.. code-block:: text

   $ curl -X POST http://192.168.1.197:8000/generate-passwords \
     -H "Content-Type: application/json" \
     -d '{"Uname": "Alice", "Byear": "1988", "Fav": "Soccer", "City": "Paris", "Hobby": "Drawing"}'

   Response:
   {
     "results": ["Alice88Draw", "SoccerParis", "ParisD1988"],
     "time_taken_seconds": 2.12
   }

See Also
--------

* :doc:`cracker` - For decrypting AES-encrypted files using a password list
* :doc:`password_sug` - For human-readable secure password suggestions
