import numpy

from statslib.methods.least_square import LS
from statslib.models.arma import ARMA

from tests.settings.autoregression import order as ar_order, parameters as ar_params
from tests.settings.moving_average import order as ma_order, parameters as ma_params
from tests.utils import list_to_vector

ls = LS()
arma = ARMA(ma_order, ma_params, ar_order, ar_params)

if __name__ == "__main__":
    length = 500
    dataset = arma.generate_time_series(length=length)
    observation_vector = list_to_vector(dataset=dataset)
    dimension_matrix = numpy.matrix([arma.dimension_vector(dataset=dataset, index=i) for i in range(0, length)])
    print(ls.estimate(observation_vector, dimension_matrix))
