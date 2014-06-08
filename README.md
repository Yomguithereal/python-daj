# daj

Are you terminally annoyed by the number of unaesthetic lines you have to write when the only thing you need is just reading and parsing some fracking data?

Well if this is the case, **daj** is made for you!

**daj**'s philosophy is to enable you to read and write popular data formats in only one simplistic line.

No more of the following nonsense:

```python
import json

with open('path/to/your-fracking-data.json', 'r') as jf:
    data = json.load(jf)
```

Now, you just write:

```python
from daj import daj

data = daj < 'path/to/your-fracking-data.json'
```

**daj** is your quick & dirty scripting companion. No more annoying boilerplate code: you start coding things that matter right now!

## Formats supported

* text
* json
* yaml
* csv
* tsv

## Reading
Note that if you do not provide a method to **daj**, this one will try to guess your format by analyzing the file's extension. So if you have a twisted mind and like to name csv files `table.json`, well first of all you are a sneaky bastard, second, just use the proper **daj** method.

```python
// Guessing the format
data = daj < 'file.json'

// Will also work with raw text
data = daj < 'file.txt'

// Using daj methods
data = daj.json < 'file.json'
data = daj.yml < 'file.yml'
data = daj.csv < 'file.csv'
data = daj.tsv < 'file.tsv'

// Needing headers for your neat CSV files?
data = daj.csvh < 'file.csv'
data = daj.tsvh < 'file.tsv'
```

## Writing

## Disclaimer
**daj** is clearly orientated toward quick & dirty data processing. This is probably a bad idea to use it in a production context and I would not vouch for that.
