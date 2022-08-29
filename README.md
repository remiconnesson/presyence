# presyence

Easily test your feature engineering functions!

Just name your test files `whatyouwant.spec.sy.py`

```python
# file : `mytest.spec.sy.py`

# these are just the necessary import
from presyence.simpletests import SimpleTest
import pandas as pd
# realcode is the code that you want to test
from realcode import identity, drop_unnamed

# start by creating a variable called TESTS as an empty list
TESTS = []

# you can declare your dataframe in-file or import them from another file
dict_dataframe = {"Unnamed: 0": [1, 2, 3, 4], "useful col": [1, 2, 4, 3]}

# this is how you add a SimpleTest to be run
TESTS += SimpleTest(
    function=identity,
    title="Identity function should return the same object",
    input=pd.DataFrame.from_dict(dict_dataframe),
    expected_output=pd.DataFrame.from_dict(dict_dataframe),
)

# another exemple
TESTS += SimpleTest(
    function=drop_unnamed,
    title="Drop Unnamed should drop the column 'Unnamed: 0'",
    input=pd.DataFrame.from_dict(dict_dataframe),
    expected_output=pd.DataFrame.from_dict(
        {k:v for k,v in dict_dataframe.items() if k != "Unnamed: 0"}
    ),
)

# then you can just run `presyence` in your project directory and it will run the test
```

for reference the content of `realcode.py` is the following:
```python
import pandas as pd

def identity(x):
    return x

def drop_unnamed(df):
    return df.drop(columns=['Unnamed: 0'])
```


- `presyence` requires python `3.10`



