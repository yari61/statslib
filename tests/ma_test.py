from statslib.models.moving_average import MovingAverage
from statslib.iface.read import read_dataset

from tests.settings.dataset import path
from tests.settings.moving_average import order, parameters

dataset = read_dataset(path=path)
dataset = [float(record[0]) for record in dataset]

moving_average = MovingAverage(order=order, parameters=parameters)

if __name__ == "__main__":
    length = 45
    dataset = moving_average.generate_time_series(length=length)
    for i in range(0, length):
        forecast = moving_average.forecast(dataset=dataset, index=i)
        real = dataset[i]
        print(forecast, real, real - forecast)
