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
### Estimate subprogram
- `-d & --data-file` : *str* -- Path to the file with the time-series dataset
- `-l & --length` : *int* -- Length of the dataset to generate
- `--ma-order` : *int* -- Moving average order
- `--ma-params` : *list* -- Moving average parameters
- `--ar-order` : *int* -- Autoregression order
- `--ar-params` : *list* -- Autoregression parameters

### Graph subprogram
- `-i` or `--index` : *int* -- Parameter index

## Example of usage
1. The following command runs the program with overriden values for *ma_order* and *ma_params* variables, and dataset would not be generated automatically but read from *tests/datasets/test.csv* file.
```
python tests/lab.py estimate -d tests/datasets/test.csv --ma-order 2 --ma-params 0 0.5 0.2
```
2. The following command outputs the time-series plot of the 3-rd parameter values
```
python tests/lab.py graph --index 3
```
