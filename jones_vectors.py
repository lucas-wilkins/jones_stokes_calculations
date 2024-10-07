import numpy as np

from dataclasses import dataclass

@dataclass
class Wave:
    E_x: float
    E_y: float
    phi_x: float
    phi_y: float

    def jones_vector(self):
        return np.array([
            self.E_x*np.exp(1j * self.phi_x),
            self.E_y*np.exp(1j * self.phi_y)
        ])

    @staticmethod
    def from_jones(jones_vector):
        E_x, E_y = np.abs(jones_vector)
        phi_x, phi_y = np.angle(jones_vector)
        return Wave(E_x, E_y, phi_x, phi_y)

    def show_ellipse(self, autoshow=True):
        """ Draw the polarisation ellipse"""
        import matplotlib.pyplot as plt

        # Basically, run for one period
        angles = np.linspace(0.0, 2*np.pi, 51)

        x = self.E_x * np.cos(angles + self.phi_x)
        y = self.E_y * np.cos(angles + self.phi_y)

        plt.plot(x, y)

        plt.axis("equal")

        if autoshow:
            plt.show()


    @property
    def delta(self) -> float:
        """ Delta calculated assuming that the delta is for E>0"""

        if np.abs(self.E_x) < 1e-10:
            return 0.0

        if np.abs(self.E_y) < 1e-10:
            return 0.0

        delta = (self.phi_x - self.phi_y)

        if self.E_x < 0:
            delta += np.pi

        if self.E_y < 0:
            delta -= np.pi

        delta %= 2 * np.pi

        if delta > np.pi:
            delta -= 2*np.pi

        elif delta <= np.pi: # Probably not necessary
            delta += 2*np.pi

        return delta


    @property
    def intensity(self):
        return self.E_x**2 + self.E_y**2

    @property
    def polarisation_angle(self):
        angle = np.atan2(self.E_y, self.E_x)
        angle %= np.pi
        return angle

    @property
    def polarisation_angle_deg(self):
        return 180*self.polarisation_angle/np.pi

    @property
    def ellipsicity(self):
        return np.sin(self.delta)

    def _polarisation_state_description(self, tol=1e-10) -> str:

        e = self.ellipsicity
        if np.abs(e) <= tol:
            return f"linear, angle={self.polarisation_angle_deg}deg"
        elif np.abs(e) >= 1-tol:
            if e > 0:
                return "right handed"
            else:
                return "left handed"
        else:
            return f"mixed, angle={self.polarisation_angle_deg}deg, ellipsicity={np.round(e, decimals=5)}"

    @property
    def description(self) -> str:
        if self.intensity < 1e-30:
            return "Wave(0)"
        else:
            return f"Wave({self._polarisation_state_description()}, intensity={np.round(self.intensity, decimals=5)})"