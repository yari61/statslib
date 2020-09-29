import sys

import numpy
import matplotlib.pyplot as plt

from statslib.models.arma import ARMA
from statslib.methods.recursive_least_square import RLS
from statslib.iface.cli import parser
from statslib.iface.read import read_dataset

from tests.settings.autoregression import order as ar_order, parameters as ar_params
from tests.settings.moving_average import order as ma_order, parameters as ma_params
from tests.utils import list_to_vector, vector_to_list

arma = ARMA(ma_order, ma_params, ar_order, ar_params)
rls = RLS()

if __name__ == "__main__":
    args = parser.parse_args(sys.argv[1:])
    length = 1000
    dataset = arma.generate_time_series(length=length)
    observation_vector = list_to_vector(dataset=dataset)
    dimension_matrix = numpy.matrix([arma.dimension_vector(dataset=dataset, index=i) for i in range(0, len(dataset))])
    params = rls.dynamic_estimate(observation_vector, dimension_matrix, list_to_vector(arma.parameters))
    plt.plot([vector_to_list(step[0][args.index])[0] for step in params])
    plt.show()
