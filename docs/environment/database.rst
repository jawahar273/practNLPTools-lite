
DataBase Environment
====================

The Database environment will be use in activing
specific property in database.

+--------------+--------------+----------------------------------------+
| Name         | Value        | Description                            |
+==============+==============+========================================+
| TABLENAME    | package_items| Table will be created under the        |
|              |              | given name and all the value stored    |
|              |              | under this table.                      |
+--------------+--------------+----------------------------------------+
| DATABASE_ECHO| DEBUG        | Show's what `sqlalchemy`               |
|              |              |  doing inside itself.                  |
+--------------+--------------+----------------------------------------+
| DATABASE_URL | db_url       | Set url which is support by DB-driver_ |
+--------------+--------------+----------------------------------------+

.. _DB-driver: https://docs.sqlalchemy.org/en/latest/dialects/


