# -------------------------------------------------------------------
# daj Reader Units Tests
# -------------------------------------------------------------------
#
#   Author: Yomguitheral
#
import unittest
from daj import daj


class ReaderTest(unittest.TestCase):

    def res(self, r):
        return 'tests/resources/%s' % r

    def test_plain(self):
        self.assertEqual(
            u'Hello World!',
            daj < self.res('hello.txt')
        )

    def test_json(self):
        self.assertEqual(
            {u'hello': u'world', u'colors': [u'yellow', u'blue']},
            daj < self.res('hello.json')
        )

        self.assertEqual(
            {u'hello': u'world', u'colors': [u'yellow', u'blue']},
            daj.json < self.res('hello.json')
        )

    def test_yaml(self):
        self.assertEqual(
            {u'hello': u'world', u'colors': [u'yellow', u'blue']},
            daj < self.res('hello.yml')
        )

        self.assertEqual(
            {u'hello': u'world', u'colors': [u'yellow', u'blue']},
            daj.yaml < self.res('hello.yml')
        )

    def test_csv(self):
        self.assertEqual(
            [['Joe', 'Dagger'], ['Elena', 'Ashcroft']],
            daj < self.res('names.csv')
        )

        self.assertEqual(
            [['Joe', 'Dagger'], ['Elena', 'Ashcroft']],
            daj.csv < self.res('names.csv')
        )

        self.assertEqual(
            [{'Firstname': 'Joe', 'Lastname': 'Dagger'}, {'Firstname': 'Elena', 'Lastname': 'Ashcroft'}],
            daj.csvh < self.res('hnames.csv')
        )

    def test_tsv(self):
        self.assertEqual(
            [['Joe', 'Dagger'], ['Elena', 'Ashcroft']],
            daj < self.res('names.tsv')
        )

        self.assertEqual(
            [['Joe', 'Dagger'], ['Elena', 'Ashcroft']],
            daj.tsv < self.res('names.tsv')
        )

        self.assertEqual(
            [{'Firstname': 'Joe', 'Lastname': 'Dagger'}, {'Firstname': 'Elena', 'Lastname': 'Ashcroft'}],
            daj.tsvh < self.res('hnames.tsv')
        )
