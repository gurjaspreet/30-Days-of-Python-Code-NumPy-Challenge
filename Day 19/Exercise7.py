import numpy as np


np.set_printoptions(suppress=True)
playway_values = np.array(
    [
        [305.0, 324.5, 283.5, 310.0, 64081.0],
        [325.5, 340.5, 320.0, 340.5, 55496.0],
        [324.0, 340.5, 315.0, 330.0, 36152.0],
        [344.0, 344.0, 310.0, 315.0, 35992.0],
        [306.5, 307.0, 291.0, 305.0, 32539.0],
        [274.0, 291.0, 250.0, 258.0, 79402.0],
        [278.0, 284.5, 256.0, 264.0, 35700.0],
        [270.0, 270.0, 238.5, 245.0, 60445.0],
        [218.0, 228.0, 196.0, 197.0, 94031.0],
        [210.0, 229.0, 198.8, 211.0, 100412.0],
        [205.0, 248.0, 197.8, 240.5, 50659.0],
        [245.0, 269.0, 232.5, 264.0, 99480.0],
        [264.0, 280.0, 251.0, 270.0, 70136.0],
        [267.0, 280.0, 267.0, 279.5, 30732.0],
        [297.5, 307.0, 280.0, 280.5, 43426.0],
        [274.0, 289.0, 258.0, 285.0, 37098.0],
        [305.0, 309.0, 296.5, 309.0, 31939.0],
        [313.0, 330.0, 295.0, 304.0, 46724.0],
        [300.0, 309.0, 295.5, 300.0, 27213.0],
        [302.0, 306.5, 290.0, 296.0, 13466.0],
        [299.0, 300.0, 287.0, 300.0, 10316.0],
        [302.5, 309.0, 302.0, 306.5, 15698.0],
    ]
)

result = playway_values[playway_values[:, 4].argsort()[::-1]][:10]
print(result)