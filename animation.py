def visualize(algorithm):
    def wrapper(arr):
        return algorithm(arr)
    wrapper.__name__ = algorithm.__name__
    return wrapper