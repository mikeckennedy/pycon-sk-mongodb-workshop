# Step 5: Insert some data

To insert data, simply create one or more instances of your objects. Set the fields. And then call `save`.

Here is one example:

```python
p = Package()
p.name = 'bs4'
p.version = "1.4.4"
p.save()
```
