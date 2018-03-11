# Step 4: Define the classes

Now you'll define a couple of the relevant classes from your data model. Here is one possible model in Python.

```python
import mongoengine
class Package(mongoengine.Document):    created = mongoengine.DateTimeField(default=datetime.datetime.now)
    name = mongoengine.StringField(required=True)
    maintainers = mongoengine.ListField(mongoengine.ObjectIdField())
    total_downloads = mongoengine.LongField(default=0)

    meta = {
        'db_alias': 'core',
        'collection': 'packages'
      }
```
