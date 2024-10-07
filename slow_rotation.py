
import numpy as np
from jones_vectors import Wave
from elements import linear_polariser_deg

import matplotlib.pyplot as plt

n_polarisers = [i for i in range(1, 51)]
intensities = []

for n in n_polarisers:
    wave = Wave(1, 0, 0, 0).jones_vector()
    angles = [90*(i+1)/n for i in range(n)]

    # print(angles)
    polarisers = [linear_polariser_deg(angle) for angle in angles]

    for p in polarisers:
        wave = np.dot(p, wave)

    # print(Wave.from_jones(wave).description)
    intensities.append(Wave.from_jones(wave).intensity)

plt.plot(n_polarisers, intensities)
plt.plot(n_polarisers, [(1-1/x)**2 for x in n_polarisers])

plt.show()