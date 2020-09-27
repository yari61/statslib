import numpy

from statslib.models.arma import ARMA
from statslib.methods.recursive_least_square import RLS
from statslib.methods.least_square import LS

from tests.settings.autoregression import order as ar_order, parameters as ar_params
from tests.settings.moving_average import order as ma_order, parameters as ma_params
from tests.utils import list_to_vector, vector_to_list

arma = ARMA(ma_order, ma_params, ar_order, ar_params)
ls = LS()
rls = RLS()

if __name__ == "__main__":
    length = 900
    dataset = arma.generate_time_series(length=length)
    observation_vector = list_to_vector(dataset=dataset)
    dimension_matrix = numpy.matrix([arma.dimension_vector(dataset=dataset, index=i) for i in range(0, length)])
    rls_params, p_matrix = rls.estimate(observation_vector, dimension_matrix, list_to_vector(arma.parameters))
    ls_params = ls.estimate(observation_vector, dimension_matrix)

    arma.update_parameters(vector_to_list(rls_params))
    print(arma.sum_error_squares(dataset=dataset), arma.r2(dataset=dataset), arma.ika(dataset=dataset))

    arma.update_parameters(vector_to_list(ls_params))
    print(arma.sum_error_squares(dataset=dataset), arma.r2(dataset=dataset), arma.ika(dataset=dataset))
