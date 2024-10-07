import numpy as np
import pytest

from jones_vectors import Wave
from elements import nothing, left_polariser, right_polariser, quarter_wave_vertical, quarter_wave_horizontal

j = Wave(1, 0, 0, 0).jones_vector()

for elem in [nothing,
             left_polariser, right_polariser,
             quarter_wave_vertical, quarter_wave_horizontal]:

    ephi = Wave.from_jones(np.dot(elem, j))

    print(ephi.description)


