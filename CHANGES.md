# 0.2.0

### Features

* Add support for list values

```yaml
doc_tools:
    - mkdocs
    - 'sphinx'
    - null
```
* Expose ``PoyoException`` in API

```python
from poyo import PoyoException
```

### Bugfixes

* Ignore dashes in lines

```yaml
---
default_context:
    foo: "hallo #welt" #Inline comment :)
    docs: true
```

# 0.1.0

First release on PyPI.

Features:

* ``parse_string()`` to load a YAML string as a Python dict
