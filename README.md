# presyence

Easily test your feature engineering functions!

Just name your test files `whatyouwant.spec.sy.py` and then run `presyence` in your project directory.

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

# another example
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


# Installation

Just run `pip install presyence` and then run `presyence` in your project directories.

- NOTE: `presyence` requires python `3.10`

# How to Use?

1. create a file ending with `.spec.sy.py`
2. in that file create an empty lists called `TESTS`
3. `from presyence.simpletests import SimpleTest`
4. Then just add `SimpleTest` to the list of `TESTS` in that file. 
5. Once you are happy with your tests, you can launch the testrunner with typing `presyence` in your CLI

# How to create a simple test?

`SimpleTest` requires 4 arguments:
1. the function you want to test
2. the input to the function (a `pandas.DataFrame` or a `pandas.Series`)
3. the expected output of the function (a `pandas.DataFrame` or a `pandas.Series`)
4. a string as title to describe what is being tested




