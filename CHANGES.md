# 0.4.0

### Features

* Add support for block comments in sections, thanks to [@jakubka][@jakubka]
  and [@hackebrot][@hackebrot] (#7)

```yaml
default_context: # foobar
    greeting: こんにちは
    # comment
    # allthethings
    docs: true

    123: 456.789
```

### Improvements

* Set up ``poyo`` logger with NullHandler to log DEBUG messages when parsing,
  thanks to [@hackebrot][@hackebrot]

### Bugfixes

* Fix an issue around section names if the line contained more than one colon
  symbol, thanks to [@gvalkov][@gvalkov] and [@hackebrot][@hackebrot] (#9)
* Fix an issue that caused partial matches to raise an error, thanks to
  [@gvalkov][@gvalkov] and [@hackebrot][@hackebrot] (#9)

[@gvalkov]: https://github.com/gvalkov
[@hackebrot]: https://github.com/hackebrot
[@jakubka]: https://github.com/jakubka


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

### Bugfixes

* Solve an issue with ``~`` character not being recognized as ``None``

[@eykd]: https://github.com/eykd
[@hackebrot]: https://github.com/hackebrot


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
