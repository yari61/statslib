from numpy import array
from numpy.random import normal


class MovingAverage(object):
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
            float: Forecast value
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

        assert len(dimension_vector) == self.order, AssertionError(f"Length of the dimension vector {len(dimension_vector)} is not equal to the order {self.order}")
        forecast_value = self.parameters[0] + sum([self.parameters[i + 1] * dimension_vector[i] for i in range(0, self.order)])
        return forecast_value

    def difference(self, dataset: list, index: int) -> list:
        """Computes the difference between the forecast value and the real value (e.g. white noise) for specific index of the time series dataset

        Args:
            dataset (list): Time series dataset
            index (int): Index number of the value to compute the difference for

        Returns:
            list: White noise
        """

        assert index >= 0
        differences = [0.0 for i in range(0, self.order)]
        for i in range(self.order, index):
            forecast_value = self._forecast(differences[len(differences)-self.order:])
            differences.append(dataset[i] - forecast_value)
        return differences

    def dimension_vector(self, dataset, index: int) -> array:
        """Creates a dimension vector for index in dataset

        Args:
            dataset ([type]): [description]
            index (int): [description]

        Returns:
            array: Dimension vector [eps(k), eps(k-1), eps(k-2), ... , eps(k-self.order)]
        """

        differences = self.difference(dataset=dataset, index=index)
        dimension_vector = [differences[i] if i >= 0 else 0 for i in range(index-1, index-self.order-1, -1)]
        return array(dimension_vector)
    
    def generate_time_series(self, length: int) -> list:
        dataset = list()
        for i in range(0, length):
            dimension_vector = self.dimension_vector(dataset=dataset, index=i)
            dataset.append(self.generate_single_value(dimension_vector=dimension_vector))
        return dataset

    def generate_single_value(self, dimension_vector: array) -> float:
        value = self._forecast(dimension_vector=dimension_vector) + normal()
        return value

    @property
    def order(self):
        return self._order

    @property
    def parameters(self):
        return self._parameters
