# 0.3.0

### Features

* Add support for blank lines and comment lines in lists, thanks to
  [@eykd][@eykd] and [@hackebrot][@hackebrot] (#5)

```yaml
doc_tools:
    # docs or didn't happen
    -    mkdocs
    - 'sphinx'

    - null
```

### Improvements

* Add tests for patterns, thanks to [@eykd][@eykd] and [@hackebrot][@hackebrot]
  (#5)

[@eykd]: https://github.com/eykd
[@hackebrot]: https://github.com/hackebrot

### Bugfixes

* Solve an issue with ``~`` character not being recognized as ``None``


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

### Features

* ``parse_string()`` to load a YAML string as a Python dict
