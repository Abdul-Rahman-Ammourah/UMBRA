AI Password Generator
====================

.. automodule:: password_gen.password_gen
   :members:
   :undoc-members:
   :show-inheritance:

API Integration
--------------

The module communicates with a local GPT-2 API endpoint:

.. list-table:: API Parameters
   :widths: 20 30 50
   :header-rows: 1

   * - Parameter
     - Type
     - Description
   * - Uname
     - str
     - Target username
   * - Byear
     - str
     - Birth year (YYYY)
   * - Fav
     - str
     - Favorite item/activity
   * - City
     - str
     - Associated city
   * - Hobby
     - str
     - Primary hobby
   * - Chunksize
     - int
     - Number to generate

Workflow Diagram
----------------

.. mermaid::

    sequenceDiagram
       User->>+CLI: Enters personal data
       CLI->>+API: Sends JSON payload
       API->>+Model: Processes request
       Model-->>-API: Returns passwords
       API-->>-CLI: Returns results
       CLI->>+Filesystem: Saves to .txt
       Filesystem-->>-User: Confirmation

Security Considerations
----------------------

.. warning::
   - Always run the API endpoint locally
   - Never expose sensitive personal data
   - Generated passwords should be encrypted at rest

Example Output
-------------

.. code-block:: text

   [SYSTEM] Initializing AI password generator...
   Enter target's name: TestUser
   ...
   [SUCCESS] Generated 100 passwords
   Time: 2.34s | Saved to: passwords_20240515_142356.txt

See Also
--------

* :doc:`password_sug` - For rule-based suggestions
* :doc:`cracker` - For strength testing