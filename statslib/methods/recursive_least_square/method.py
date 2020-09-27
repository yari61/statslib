from numpy import matrix, array, identity, dot, append


class RecursiveLeastSquare(object):
    def estimate(self, observation_vector: matrix, dimension_matrix: matrix, params: matrix, index: int = None) -> tuple:
        """Estimates regression parameters using recursive least squares method

        Args:
            observation_vector (matrix): [description]
            dimension_matrix (matrix): [description]
            params (matrix): [description]
            index (int, optional): [description]. Defaults to None.

        Returns:
            tuple: [description]
        """
        index = index if index is not None else len(observation_vector)-1
        if index == 0:
            p_matrix = dot(len(observation_vector), identity(len(params)))
            return params, p_matrix
        params, p_matrix = self.estimate(
            observation_vector=observation_vector, 
            dimension_matrix=dimension_matrix, 
            params=params,
            index=index-1
        )
        p_matrix = p_matrix - dot(dot(dot(p_matrix, dimension_matrix[index].getT()), dimension_matrix[index]), p_matrix) / (1 + dot(dot(dimension_matrix[index], p_matrix), dimension_matrix[index].getT()))
        params = params + dot(dot(p_matrix, dimension_matrix[index].getT()), observation_vector[index] - dot(dimension_matrix[index], params))
        return params, p_matrix
