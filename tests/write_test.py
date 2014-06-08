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

        self.assertEqual(
            j,
            daj < self.res('hello.json')
        )

    def tearDown(self):
        shutil.rmtree(self.folder)
