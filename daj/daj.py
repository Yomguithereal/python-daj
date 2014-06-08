# -------------------------------------------------------------------
# daj Main File
# -------------------------------------------------------------------
#
#   Author: Yomguitheral
#

# Dependencies
#=============
import os
import codecs
import csv
import json
import yaml


# Helpers
#========
def extension(filename):
    _, ext = os.path.splitext(filename)
    return ext


# Abstract classes
#=================
class Reader(object):
    ''' The Reader class aims at reading popular data file and returning
    parsed data. '''

    def read(self, filename, encoding='utf-8'):
        with codecs.open(filename, 'r', encoding=encoding) as f:
            return f.read()

    def readJson(self, filename):
        return json.loads(self.read(filename))

    def readYaml(self, filename):
        return yaml.load(self.read(filename))


class Writer(object):
    ''' The Writer class aims at writing popular data file formats. '''
    pass


# Main class
#===========
class Daj(object):

    supported = [
        '.json',
        '.yml',
        '.yaml',
        '.csv',
        '.tsv'
    ]

    reader = Reader()

    # Call operator as writer
    def __call__(self, data):
        return Writer()

    # Less than operator as read file
    def __lt__(self, filename):
        ext = extension(filename)

        if ext in self.supported:
            if ext == '.json':
                return self.reader.readJson(filename)
            elif ext == '.yml' or ext == '.yaml':
                return self.reader.readYaml(filename)
            elif ext == '.csv':
                return self.reader.readCsv(filename)
            else:
                return self.reader.readTsv(filename)
        else:
            return self.reader.read(filename)


# Exporting an instance of daj
daj = Daj()
