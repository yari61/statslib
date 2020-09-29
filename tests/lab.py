import json

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


def count_metrics(dataset: list, model: ARMA, method: str = None):
    result = {
        "method": method,
        "ar_order": arma.ar.order,
        "ma_order": arma.ma.order,
        "rss": arma.sum_error_squares(dataset=dataset),
        "r2": arma.r2(dataset=dataset),
        "ika": arma.ika(dataset=dataset)
    }
    return result

if __name__ == "__main__":
    length = 1000

    for ar_order_i in range(1, ar_order + 1):
        arma.ar._order = ar_order_i
        for ma_order_i in range(1, ma_order + 1):
            arma.ma._order = ma_order_i
            
            arma.ma._parameters = ma_params
            arma.ar._parameters = ar_params

            dataset = arma.generate_time_series(length=length)
            observation_vector = list_to_vector(dataset=dataset)
            dimension_matrix = numpy.matrix([arma.dimension_vector(dataset=dataset, index=i) for i in range(0, length)])
            rls_params = rls.estimate(observation_vector, dimension_matrix, list_to_vector(arma.parameters))
            ls_params = ls.estimate(observation_vector, dimension_matrix)

            arma.update_parameters(vector_to_list(rls_params))
            print(json.dumps(count_metrics(dataset=dataset, model=arma, method="RLS")))

            arma.update_parameters(vector_to_list(ls_params))
            print(json.dumps(count_metrics(dataset=dataset, model=arma, method="LS")))
