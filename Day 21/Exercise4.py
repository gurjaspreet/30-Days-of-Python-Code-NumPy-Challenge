import numpy as np


np.random.seed(20)
arr = np.array(
    [
        [0.88389311],
        [0.19586502],
        [0.35753652],
        [-2.34326191],
        [-1.08483259],
        [0.55969629],
        [0.93946935],
        [-0.97848104],
        [0.50309684],
        [0.40641447],
    ]
)

arr = np.where(arr == np.min(arr), np.nan, arr)
print(arr)