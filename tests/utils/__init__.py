import numpy


def list_to_vector(dataset: list) -> numpy.matrix:
    return numpy.matrix(dataset).getT()


def vector_to_list(vector: numpy.matrix) -> list:
    assert len(vector.getT()) == 1
    return [i for i in vector.flat]
