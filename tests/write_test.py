# -------------------------------------------------------------------
# daj Writer Units Tests
# -------------------------------------------------------------------
#
#   Author: Yomguitheral
#
import os
import unittest
import shutil
from daj import daj

class WriterTest(unittest.TestCase):

    folder = '.tests'

    def res(self, r):
        return '%s/%s' % (self.folder, r)

    def setUp(self):
        try:
            os.mkdir(self.folder)
        except:
            pass

    def test_plain(self):
        daj('Hello World!') > self.res('hello.txt')

        self.assertEqual(
            'Hello World!',
            daj < self.res('hello.txt')
        )

    def test_json(self):
        j = {u'hello': u'world'}
        daj(j) > self.res('hello.json')
        daj.json(j) > self.res('hello2.json')
        daj.pjson(j) > self.res('pretty_hello.json')

        self.assertEqual(j, daj < self.res('hello.json'))
        self.assertEqual(j, daj < self.res('hello2.json'))
        self.assertEqual(j, daj < self.res('pretty_hello.json'))

    def test_yaml(self):
        j = {u'hello': {u'location': u'world'}, u'colors': [u'yellow', u'blue']}
        daj(j) > self.res('hello.yml')
        daj.yml(j) > self.res('hello2.yml')

        self.assertEqual(j, daj < self.res('hello.yml'))
        self.assertEqual(j, daj < self.res('hello2.yml'))

    def test_csv(self):
        a = [['Joe', 'Dagger'], ['Elena', 'Ashcroft']]
        o = [{'Firstname': 'Joe', 'Lastname': 'Dagger'}, {'Firstname': 'Elena', 'Lastname': 'Ashcroft'}]

        daj(a) > self.res('names.csv')
        daj(o) > self.res('hnames.csv')
        daj.csv(a) > self.res('names2.csv')
        daj.csv(o) > self.res('hnames2.csv')

        self.assertEqual(a, daj < self.res('names.csv'))
        self.assertEqual(a, daj < self.res('names2.csv'))
        self.assertEqual(o, daj.csvh < self.res('hnames.csv'))
        self.assertEqual(o, daj.csvh < self.res('hnames2.csv'))

    def test_tsv(self):
        a = [['Joe', 'Dagger'], ['Elena', 'Ashcroft']]
        o = [{'Firstname': 'Joe', 'Lastname': 'Dagger'}, {'Firstname': 'Elena', 'Lastname': 'Ashcroft'}]

        daj(a) > self.res('names.tsv')
        daj(o) > self.res('hnames.tsv')
        daj.tsv(a) > self.res('names2.tsv')
        daj.tsv(o) > self.res('hnames2.tsv')

        self.assertEqual(a, daj < self.res('names.tsv'))
        self.assertEqual(a, daj < self.res('names2.tsv'))
        self.assertEqual(o, daj.tsvh < self.res('hnames.tsv'))
        self.assertEqual(o, daj.tsvh < self.res('hnames2.tsv'))

    def tearDown(self):
        shutil.rmtree(self.folder)
