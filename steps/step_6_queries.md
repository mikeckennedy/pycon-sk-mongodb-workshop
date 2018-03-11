# Step 6: Query some packages

Now that you have data, write some code to retrieve it from the database. Here are two examples of relevant queries.

## A single document

```python
def find_package_by_name(name: str) -> Optional[Package]:
    p = Package.objects(name=name).first()
    return p
```

## All maintainers of a package

```python
def maintainers(package: Package) -> List[User]:
    users = User.objects(id__in=package.maintainers)
    return list(users)
```

## Top downloads

```python
def popular_packages(limit: int) -> List[Package]:
    packages = Package.objects().order_by('-total_downloads').limit(limit)
    return list(packages)
```
