# pretty print

pretty print data in mysql format

## Usage


- to stdout

```python
from pretty_print import pretty_print

example_fields = ('CompanyName', 'ContactName', 'Address', 'City')
example_data_list = [
    {
        'CompanyName': u'Alfreds Futterkiste',
        'ContactName': u'Maria Anders',
        'Address': u'Obere Str. 57',
        'City': u'Berlin'
    },
    {
        'CompanyName': u'Berglunds snabbköp',
        'ContactName': u'Christina Berglund',
        'Address': u'Berguvsvägen 8',
        'City': u'Luleå'
    },
    {
        'CompanyName': u'Centro comercial Moctezuma',
        'ContactName': u'Francisco Chang',
        'Address': u'Sierras de Granada 9993',
        'City': u'México D.F.'
    },
    {
        'CompanyName': u'Galería del gastrónomo',
        'ContactName': u'Eduardo Saavedra',
        'Address': u'Rambla de Cataluña, 23',
        'City': u'Barcelona'
    },
    {
        'CompanyName': u'Island Trading',
        'ContactName': u'Helen Bennett',
        'Address': u'Garden House Crowther Way',
        'City': u'Cowes'
    },
]

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
from io import StringIO
    
str_io = StringIO()
pretty_print(example_fields, example_data_list, str_io)

# do something with str_io
```