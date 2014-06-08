# -------------------------------------------------------------------
# daj Reader Units Tests
# -------------------------------------------------------------------
#
#   Author: Yomguitheral
#
import unittest
from daj import daj


class ReaderTest(unittest.TestCase):

    def res(self, resource):
        return 'tests/resources/%s' % resource

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

    def test_yaml(self):
        self.assertEqual(
            {u'hello': u'world', u'colors': [u'yellow', u'blue']},
            daj < self.res('hello.yml')
        )
