import numpy.linalg
from numpy import matrix, array, dot


class LeastSquare(object):
    @staticmethod
    def estimate(observation_vector: matrix, dimension_matrix: matrix) -> matrix:
        parameters = dot(dot(numpy.linalg.inv(dot(dimension_matrix.getT(), dimension_matrix)), dimension_matrix.getT()), observation_vector)
        return parameters
