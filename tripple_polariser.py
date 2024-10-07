""" Classic three polariser experiment

Begin with two polarisers at 90 degrees to each other, no light
Add an extra at 45 degrees between, and you get light though
"""

import numpy as np
from jones_vectors import Wave
from elements import linear_polariser_deg

double = [linear_polariser_deg(0), linear_polariser_deg(90)]
tripple = [linear_polariser_deg(0), linear_polariser_deg(45), linear_polariser_deg(90)]

def apply_element_series(series):
    x_component = Wave(1, 0, 0, 0)
    y_component = Wave(0, 1, 0, 0)

    print("  Start Vectors")
    components = [x_component.jones_vector(),
                  y_component.jones_vector()]

    for i, element in enumerate(series):
        components = [np.dot(element, component) for component in components]
        print(f"  After element {i+1}")
        for component in components:
            print("    ", Wave.from_jones(component).description)

print("0 then 90")
apply_element_series(double)

print("0, then 45, then 90")
apply_element_series(tripple)