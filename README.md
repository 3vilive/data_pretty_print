# pretty print

## Usage


- to stdout

```python
from pretty_print import pretty_print

example_fields = ...
example_data_list = ...

pretty_print(example_fields, example_data_list)
```

result

```
+----------------------------+--------------------+---------------------------+-------------+
| CompanyName                | ContactName        | Address                   | City        |
+----------------------------+--------------------+---------------------------+-------------+
|        Alfreds Futterkiste |       Maria Anders |             Obere Str. 57 |      Berlin |
|         Berglunds snabbköp | Christina Berglund |            Berguvsvägen 8 |       Luleå |
| Centro comercial Moctezuma |    Francisco Chang |   Sierras de Granada 9993 | México D.F. |
|     Galería del gastrónomo |   Eduardo Saavedra |    Rambla de Cataluña, 23 |   Barcelona |
|             Island Trading |      Helen Bennett | Garden House Crowther Way |       Cowes |
+----------------------------+--------------------+---------------------------+-------------+
```

- to file

```python
with open('example_file', 'w') as f:
    pretty_print(example_fields, example_data_list, f)
```

- StringIO is also available
```python
from StringIO import StringIO
    
str_io = StringIO()
pretty_print(example_fields, example_data_list, str_io)

# do something with str_io
```