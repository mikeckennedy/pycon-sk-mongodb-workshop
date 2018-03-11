# MongoDB workshop at PyCon 2018

This step is about connecting to MongoDB. You'll need to call this code once and only once at the start of your program.

```python
import mongoenginealias_core = 'core'db = 'pypi'
mongoengine.register_connection(alias=alias_core, name=db)
```