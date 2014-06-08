[![Build Status](https://travis-ci.org/Yomguithereal/python-daj.svg)](https://travis-ci.org/Yomguithereal/python-daj)

# daj

Are you terminally annoyed by the number of unaesthetic lines you have to write when the only thing you need is just reading and parsing some fracking data?

Well if this is the case, **daj** is made for you!

**daj**'s philosophy is to enable you to read and write popular data formats in one simplistic line.

No more of the following nonsense:

```python
import codecs
import json

with codecs.open('path/to/your-fracking-data.json', 'r', encoding='utf-8') as jf:
    data = json.load(jf)
```

Now, you just write:

```python
from daj import daj

data = daj < 'path/to/your-fracking-data.json'
```

**daj** is your quick & dirty scripting companion. No more annoying boilerplate code: you start coding things that matter right now!

## Installation

With pip

```python
pip install daj
```

To install the latest dev version
```bash
pip install git+https://github.com/Yomguithereal/python-daj.git
```

## Formats supported

* plain text
* json
* yaml
* csv
* tsv

## Reading
Note that if you do not provide a method to **daj**, this one will try to guess your format by analyzing the file's extension.

So if you have a twisted mind and like to name csv files `table.json`, well first of all you are a sneaky bastard, second, just use the proper **daj** method.

```python
# Guessing the format
data = daj < 'file.json'

# Will also work with raw text
data = daj < 'file.txt'

# Using daj methods
data = daj.json < 'file.json'
data = daj.yml < 'file.yml'
data = daj.csv < 'file.csv'
data = daj.tsv < 'file.tsv'

# Needing headers for your neat CSV files?
data = daj.csvh < 'file.csv'
data = daj.tsvh < 'file.tsv'
```

## Writing
As for reading, **daj** will try to guess the correct format for your data based on the extension of the file.

```python
# Writing some data
daj(data) > 'file.json'

# Will also work with raw text
daj(data) > 'file.txt'

# Using daj methods
daj.json(data) > 'file.json'
daj.yml(data) > 'file.yml'

# If you want to ouput a pretty printed json
daj.pjson(data) > 'prettyfile.json'

# For csv, you can give an array of arrays or an array of objects
# If an array of objects is given, daj will output a csv with headers.
daj.csv(data) > 'file.csv'
daj.tsv(data) > 'file.tsv'
```

## Disclaimer
**daj** is clearly orientated toward quick & dirty data processing. This is probably a bad idea to use it in a production context and I would not vouch for that.

## Contribution
Contribution are more than welcome, be sure to add relevant unit tests and pass them all before subitting any code.

```bash
# To install dev environment (preferably in a virtualenv)
pip install -r requirements.txt

# To run unit tests
./runtests
```
