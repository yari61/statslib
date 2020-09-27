import csv


def read_dataset(path: str, delimiter: str = None):
    delimiter = delimiter or ","
    with open(path, mode="r") as csv_file:
        reader = csv.reader(csv_file, delimiter=delimiter)
        for record in reader:
            yield record
