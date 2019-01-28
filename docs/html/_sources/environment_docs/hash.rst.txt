
Hash Environment
================

Setting environment for hash property for generation and setting limit length.

+---------------+--------------+----------------------------------------+
| Name          | Value        | Description                            |
+===============+==============+========================================+
| HASH_VALUE_LEN| 10           | Setting `VARCHAR` limit to database.   |
+---------------+--------------+----------------------------------------+
| HASH_CLASS    | hashlib.md5  | Standard  python hash class will be    |
|               |              | used as default hash generator. By     |
|               |              | this approch user has the power to 3rd |
|               |              | party libery which they like with no   |
|               |              | problem(note: it should be             |
|               |              | compartable with standard hash libery  |
|               |              | of python.[Eg: xxhash]                 |
+---------------+--------------+----------------------------------------+