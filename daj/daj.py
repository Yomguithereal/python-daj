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
import sys
import csv
import json
import yaml


# Helpers
#========
PY2 = sys.version_info[0] == 2

def extension(filename):
    _, ext = os.path.splitext(filename)
    return ext

def is_string(variable):
    if PY2:
        return isinstance(variable, basestring)
    else:
        return isinstance(variable, str)


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

    def readCsv(self, filename, encoding='utf-8', delimiter=',', headers=False):
        with codecs.open(filename, 'r', encoding=encoding) as f:
            if headers:
                reader = csv.reader(f, delimiter=delimiter)
                h = next(reader)
                a = []
                for r in reader:
                    o = {}
                    for j, e in enumerate(r):
                        o[h[j]] = e
                    a.append(o)
                return a
            else:
                return [i for i in csv.reader(f, delimiter=delimiter)]

    def readTsv(self, filename, headers=False):
        return self.readCsv(filename, delimiter='\t', headers=headers)


class Writer(object):
    ''' The Writer class aims at writing popular data file formats. '''

    defaultIndent = 2

    def __init__(self, data, kind):
        self.data = data
        self.kind = kind

    # Write hub
    def write(self, ext, filename):
        ext = self.kind or ext

        if is_string(self.data):
            self.writePlain(filename, self.data)
        elif ext == '.json':
            self.writeJson(filename)

    def writePlain(self, filename, data):
        with open(filename, 'w') as f:
            f.write(data)

    def writeJson(self, filename, indent=None):
        self.writePlain(filename, json.dumps(self.data, indent=None))

    # Retrieving the filename though greater than
    def __gt__(self, filename):
        ext = extension(filename)
        self.write(ext, filename)


# Main class
#===========
class Daj(object):

    # Properties
    reader = Reader()

    # Constructor
    def __init__(self, kind=None):
        self.kind = kind


    # Reading
    #--------

    # Reader abstract
    def read(self, ext, filename):
        ext = self.kind or ext

        if ext == '.json':
            return self.reader.readJson(filename)
        elif ext == '.yml' or ext == '.yaml':
            return self.reader.readYaml(filename)
        elif ext == '.csv':
            return self.reader.readCsv(filename)
        elif ext == '.tsv':
            return self.reader.readTsv(filename)
        elif ext == '.csvh':
            return self.reader.readCsv(filename, headers=True)
        elif ext == '.tsvh':
            return self.reader.readTsv(filename, headers=True)
        else:
            return self.reader.read(filename)

    # Less than operator as read file
    def __lt__(self, filename):
        ext = extension(filename)
        return self.read(ext, filename)


    # Writing
    #--------

    # Call operator as writer
    def __call__(self, data):
        return Writer(data, self.kind)


    # Methods
    #--------

    @property
    def json(self):
        return Daj('.json')

    @property
    def yaml(self):
        return Daj('.yml')

    @property
    def yml(self):
        return Daj('.yml')

    @property
    def csv(self):
        return Daj('.csv')

    @property
    def csvh(self):
        return Daj('.csvh')

    @property
    def tsv(self):
        return Daj('.tsv')

    @property
    def tsvh(self):
        return Daj('.tsvh')

# Exporting an instance of daj
daj = Daj()
