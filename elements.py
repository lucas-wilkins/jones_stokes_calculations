import numpy as np

nothing = np.array([
    [1, 0],
    [0, 1]
])

linear_polariser_x = np.array([
    [1, 0],
    [0, 0]
])

linear_polariser_y = np.array([
    [0, 0],
    [0, 1]
])

def linear_polariser(theta):
    c = np.cos(theta)
    s = np.sin(theta)

    return np.array([
        [c*c, c*s],
        [s*c, s*s]
    ])

def linear_polariser_deg(theta_deg):
    return linear_polariser(np.pi*theta_deg/180)

right_polariser = 0.5 * np.array([
    [1, 1j],
    [-1j, 1]
])

left_polariser = 0.5 * np.array([
    [1, -1j],
    [1j, 1]
])

quarter_wave_vertical = np.exp(0.25j * np.pi) * np.array([[1, 0], [0, -1j]])
quarter_wave_horizontal = np.exp(-0.25j * np.pi) * np.array([[1, 0], [0, 1j]])
