# coding: utf8

import sys
from numbers import Number

_ver = sys.version_info

is_py2 = (_ver[0] == 2)
is_py3 = (_ver[0] == 3)


if is_py3:
    unicode = str


DEFAULT_SPACE_PADDING = 2
PLUS_SIGN = '+'
ROW_SIGN = '-'
COLUMN_SIGN = '|'


class Align:
    LEFT_ALIGN = 0
    RIGHT_ALIGN = 1


class Helper:
    @staticmethod
    def special_len(obj):
        if isinstance(obj, Number):
            return len(str(obj))
        elif isinstance(obj, str):
            return len(obj)
        elif isinstance(obj, unicode):
            return len(obj)

    @staticmethod
    def special_stringify(obj):
        if isinstance(obj, Number):
            return str(obj)
        elif isinstance(obj, unicode):
            return unicode(obj)
        elif isinstance(obj, str):
            return str(obj)


class PrettyDataPrintContext:
    def __init__(self, fields, data_list):
        self.fields = fields
        self.data_list = data_list

        self.fields_width = [0 for _ in range(len(self.fields))]

        for pos, field in enumerate(self.fields):
            for data in data_list:
                cur_field = data[field]
                self.fields_width[pos] = max(self.fields_width[pos], Helper.special_len(cur_field))

            self.fields_width[pos] = max(self.fields_width[pos], Helper.special_len(field)) + DEFAULT_SPACE_PADDING

    def __iter__(self):
        yield tuple(self.fields)
        for data in self.data_list:
            yield tuple(data[field] for field in self.fields)


class PrettyDataPainter:
    def __init__(self, fields, data_list, fp=None):
        self.ctx = PrettyDataPrintContext(fields, data_list)
        self.fields_width = self.ctx.fields_width

        if fp is None:
            self.fp = sys.stdout
        else:
            self.fp = fp

    def paint(self):
        gen = iter(self.ctx)

        # headers
        self._paint_split_row()
        headers = next(gen)
        self._paint_row(headers)
        self._paint_split_row()

        for fields in gen:
            self._paint_row(fields, align=Align.RIGHT_ALIGN)
        else:
            self._paint_split_row()

    def _write_fp(self, content):
        if is_py2:
            self.fp.write(content.encode('utf8'))
        elif is_py3:
            self.fp.write(content)

    def _paint_row(self, fields, align=Align.LEFT_ALIGN):
        for pos, field in enumerate(fields):
            width = self.fields_width[pos]

            if align == Align.LEFT_ALIGN:
                paint_body = str(field) + ' ' * (width - Helper.special_len(field) - DEFAULT_SPACE_PADDING)

            elif align == Align.RIGHT_ALIGN:
                paint_body = ' ' * (width - Helper.special_len(field) - DEFAULT_SPACE_PADDING) + Helper.special_stringify(field)

            else:
                paint_body = ' ' * width

            self._write_fp(COLUMN_SIGN + ' ' + paint_body + ' ')

        else:
            self._write_fp(COLUMN_SIGN + '\n')

    def _paint_split_row(self):
        for field_width in self.fields_width:
            self._write_fp(PLUS_SIGN + ROW_SIGN * field_width)
        else:
            self._write_fp(PLUS_SIGN + '\n')


def pretty_print(fields, data_list, fp=None):
    painter = PrettyDataPainter(fields, data_list, fp)
    painter.paint()


def example():
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

    with open('example_file', 'w') as f:
        pretty_print(example_fields, example_data_list, f)

    from io import StringIO

    str_io = StringIO()
    pretty_print(example_fields, example_data_list, str_io)
    str_io.seek(0)

    print(str_io.read())


if __name__ == '__main__':
    example()