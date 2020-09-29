# Installation
To install this package run one of the following commands from your python environment:

```
pip install -e https://github.com/yari61/statslib.git#egg=statslib
```
or
```
git clone https://github.com/yari61/statslib.git
cd statslib
pip install .
```

# Quick start
To get the result for your lab variation you just have to change parameters in `tests/settings/autoregression.py` and `tests/settings/moving_average.py` which stand for `a[0], a[1], a[2], ... , a[n]` and `b[1], b[2], ... , b[n]` parameters respectively.
Then you can just execute the following command:
```
python tests/lab.py estimate
```

# Command line interface
- `-d & --data-file` : *str*
- `-l & --length` : *int*
- `--ma-order` : *int*
- `--ma-params` : *list*
- `--ar-order` : *int*
- `--ar-params` : *list*

## Example of usage
The following command runs the program with overriden values for *ma_order* and *ma_params* variables, and dataset would not be generated automatically but read from *tests/datasets/test.csv* file.
```
python tests/lab.py estimate -d tests/datasets/test.csv --ma-order 2 --ma-params 0 0.5 0.2
```
