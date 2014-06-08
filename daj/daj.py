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
        elif ext == '.pjson':
            self.writeJson(filename, indent=self.defaultIndent)
        elif ext == '.yml' or ext == '.yaml':
            self.writeYaml(filename)
        elif ext == '.csv' or ext == '.csvh':
            self.writeCsv(filename)
        elif ext == '.tsv' or ext == '.tsvh':
            self.writeCsv(filename, delimiter='\t')
        else:
            self.writePlain(filename, self.data)

    def writePlain(self, filename, data):
        with codecs.open(filename, 'w', encoding='utf-8') as f:
            f.write(data)

    def writeJson(self, filename, indent=None):
        self.writePlain(filename, json.dumps(self.data, indent=indent))

    def writeYaml(self, filename, indent=None):
        self.writePlain(filename, yaml.safe_dump(self.data, indent=indent, default_flow_style=False))

    def writeCsv(self, filename, delimiter=','):
        headers = isinstance(self.data[0], dict) and list(self.data[0].keys())

        with codecs.open(filename, 'w', encoding='utf-8') as f:
            w = csv.writer(f, delimiter=delimiter)
            if headers:
                w.writerow(headers)
            for r in self.data:
                if headers:
                    w.writerow([r[i] for i in headers])
                else:
                    w.writerow(r)

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

        if ext == '.json' or ext == '.pjson':
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
    def pjson(self):
        return Daj('.pjson')

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
