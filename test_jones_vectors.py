import pytest
import numpy as np
from numpy.ma.testutils import approx

from jones_vectors import Wave

twopi = 2*np.pi

@pytest.mark.parametrize('E_x', [-2, -1, 0, 1, 2])
@pytest.mark.parametrize('E_y', [-2, -1, 0, 1, 2])
@pytest.mark.parametrize('phi_x', [0, 1])
@pytest.mark.parametrize('phi_y', [0, 1])
def test_forward_back_magnitude(E_x: float, E_y: float, phi_x: float, phi_y: float):
    jones = Wave(E_x, E_y, phi_x, phi_y).jones_vector()
    ephi = Wave.from_jones(jones)

    assert np.abs(ephi.E_x) == pytest.approx(np.abs(E_x), rel=1e-10)
    assert np.abs(ephi.E_y) == pytest.approx(np.abs(E_y), rel=1e-10)


@pytest.mark.parametrize('E_x', [-1, 1])
@pytest.mark.parametrize('E_y', [-1, 1])
@pytest.mark.parametrize('phi_x', np.arange(-10, 10))
@pytest.mark.parametrize('phi_y', np.arange(-10, 10))
def test_deltas(E_x: float, E_y: float, phi_x: float, phi_y: float):
    ephi1 = Wave(E_x, E_y, phi_x, phi_y)
    jones = ephi1.jones_vector()
    ephi2 = Wave.from_jones(jones)

    assert ephi1.delta == pytest.approx(ephi2.delta, abs=1e-10)

