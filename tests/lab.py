import json
import sys

import numpy
import matplotlib.pyplot as plt

from statslib.models.arma import ARMA
from statslib.methods.recursive_least_square import RLS
from statslib.methods.least_square import LS
from statslib.iface.cli import parser
from statslib.iface.read import read_dataset

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
    args = parser.parse_args(sys.argv[1:])
    if args.which == "estimate":
        length = args.length or 500
        ar_order = args.ar_order or ar_order
        ar_params = args.ar_params or ar_params
        ma_order = args.ma_order or ma_order
        ma_params = args.ma_params or ma_params

        for ar_order_i in range(1, ar_order + 1):
            arma.ar._order = ar_order_i
            for ma_order_i in range(1, ma_order + 1):
                arma.ma._order = ma_order_i

                arma.ma._parameters = ma_params
                arma.ar._parameters = ar_params

                dataset = read_dataset(args.data_file) if args.data_file else arma.generate_time_series(length=length)
                observation_vector = list_to_vector(dataset=dataset)
                dimension_matrix = numpy.matrix([arma.dimension_vector(dataset=dataset, index=i) for i in range(0, len(dataset))])
                rls_params = rls.estimate(observation_vector, dimension_matrix, list_to_vector(arma.parameters))
                ls_params = ls.estimate(observation_vector, dimension_matrix)

                arma.update_parameters(vector_to_list(rls_params))
                print(json.dumps(count_metrics(dataset=dataset, model=arma, method="RLS")))

                arma.update_parameters(vector_to_list(ls_params))
                print(json.dumps(count_metrics(dataset=dataset, model=arma, method="LS")))
    elif args.which == "graph":
        length = 1000
        dataset = arma.generate_time_series(length=length)
        observation_vector = list_to_vector(dataset=dataset)
        dimension_matrix = numpy.matrix([arma.dimension_vector(dataset=dataset, index=i) for i in range(0, len(dataset))])
        params = rls.dynamic_estimate(observation_vector, dimension_matrix, list_to_vector(arma.parameters))
        plt.plot([vector_to_list(step[0][args.index])[0] for step in params])
        plt.show()
