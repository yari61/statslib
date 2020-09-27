import json

from statslib.models.autoregression import Autoregression
from statslib.iface.read import read_dataset

from tests.settings.dataset import path
from tests.settings.autoregression import order, parameters

dataset = read_dataset(path=path)
dataset = [float(record[0]) for record in dataset]

autoregression = Autoregression(order=order, parameters=parameters)

if __name__ == "__main__":
    length = 45
    dataset = autoregression.generate_time_series(length=length)
    for i in range(0, length):
        forecast = autoregression.forecast(dataset=dataset, index=i)
        real = dataset[i]
        print(round(forecast, 2), round(real, 2), round(real - forecast, 2))
