from numpy import array
from numpy.random import normal


class Autoregression(object):
    __slots__ = ("_order", "_parameters")

    def __init__(self, order: int, parameters):
        self._order = order
        self._parameters = parameters

    def forecast(self, dataset: list, index: int) -> float:
        """Computes the forecast value for specific index of the time series dataset

        Args:
            dataset (list): Time series dataset
            index (int): Index number of the value to forecast

        Returns:
            float: forecast value
        """

        dimension_vector = self.dimension_vector(dataset=dataset, index=index)
        forecast_value = self._forecast(dimension_vector=dimension_vector)
        return forecast_value
    
    def _forecast(self, dimension_vector: array) -> float:
        """Makes a forecast of the value based on dimension vector

        Args:
            dimension_vector (array): Dimension vector

        Returns:
            float: Forecast value
        """

        assert len(dimension_vector) == self.order + 1
        forecast_value = sum([self.parameters[i] * dimension_vector[i] for i in range(0, self.order + 1)])
        return forecast_value

    def difference(self, dataset, index: int) -> float:
        """Computes the difference between the forecast value and the real value (e.g. white noise) for specific index of the time series dataset

        Args:
            dataset (:class:`Iterable`): the time series dataset
            index (int): index number of the value to compute the difference for

        Returns:
            float: white noise
        """

        forecast_value = self.forecast(dataset=dataset, index=index)
        difference = dataset[index] - forecast_value
        return difference

    def dimension_vector(self, dataset: list, index: int) -> array:
        """Creates a dimension vector for index in dataset

        Args:
            dataset (list): [description]
            index (int): [description]

        Returns:
            array: dimension vector [1, y(k-1), y(k-2), ... , y(k-self.order)]
        """

        dimension_vector = [1]
        dimension_vector.extend(
            [dataset[i] if i >= 0 else 0 for i in range(index-1, index-self.order-1, -1)]
        )
        return array(dimension_vector)

    def generate_time_series(self, length: int) -> list:
        dataset = list()
        for i in range(0, length):
            dimension_vector = self.dimension_vector(dataset=dataset, index=i)
            dataset.append(self.generate_single_value(dimension_vector=dimension_vector))
        return dataset

    def generate_single_value(self, dimension_vector: array) -> float:
        value = self.parameters[0] + normal() + sum([self.parameters[i]*dimension_vector[i] for i in range(1, self.order + 1)])
        return value

    @property
    def order(self):
        return self._order

    @property
    def parameters(self):
        return self._parameters
