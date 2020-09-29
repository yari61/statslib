import numpy
from numpy import array
from numpy.random import normal

from ..autoregression.model import Autoregression
from ..moving_average.model import MovingAverage


class ARMA(object):
    __slots__ = ("_moving_average", "_autoregression")

    def __init__(self, ma_order, ma_params, ar_order, ar_params):
        self._moving_average = MovingAverage(order=ma_order, parameters=ma_params)
        self._autoregression = Autoregression(order=ar_order, parameters=ar_params)
    
    def dimension_vector(self, dataset, index):
        return numpy.append(self.ar.dimension_vector(dataset, index), self.ma.dimension_vector(dataset, index))

    def forecast(self, dataset, index) -> float:
        return self.ma.forecast(dataset=dataset, index=index) + self.ar.forecast(dataset=dataset, index=index)

    def difference(self, dataset, index) -> float:
        forecast = self.forecast(dataset=dataset, index=index)
        return dataset[index] - forecast

    def sum_error_squares(self, dataset: list) -> float:
        return sum([self.difference(dataset, i)**2 for i in range(0, len(dataset))])

    def generate_time_series(self, length: int) -> list:
        dataset = list()
        for i in range(0, length):
            value = self.generate_single_value(
                ma_dimension_vector=self.ma.dimension_vector(dataset=dataset, index=i),
                ar_dimension_vector=self.ar.dimension_vector(dataset=dataset, index=i)
            )
            dataset.append(value)
        return dataset

    def generate_single_value(self, ma_dimension_vector: array, ar_dimension_vector: array) -> float:
        value = self.ma._forecast(dimension_vector=ma_dimension_vector) + self.ar._forecast(dimension_vector=ar_dimension_vector) + normal()
        return value

    def update_parameters(self, parameters: list):
        self.ar._parameters = parameters[:self.ar.order + 1]
        self.ma._parameters = [1] + parameters[self.ar.order + 1:]

    def ika(self, dataset: list):
        return 2 * len(self.parameters) - len(dataset) * numpy.log(self.sum_error_squares(dataset=dataset))

    def r2(self, dataset: list):
        mean_dataset = numpy.mean(dataset)
        return 1 - self.sum_error_squares(dataset=dataset) / sum((dataset[i] - mean_dataset) ** 2 for i in range(0, len(dataset)))

    @property
    def parameters(self):
        return self.ar.parameters + self.ma.parameters[1:]

    @property
    def ma(self) -> MovingAverage:
        return self._moving_average

    @property
    def ar(self) -> Autoregression:
        return self._autoregression
