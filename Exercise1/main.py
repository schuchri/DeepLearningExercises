import numpy as np
import matplotlib.pyplot as plot
from Exercise1 import circle as circ
from Exercise1 import checkers as check
from Exercise1 import spectrum as spec

#circle1 = circ.Circle(1, 1, [8])

checker = check.Checker(1, 1, 8)
checker.draw()
checker.show()

#circle1.draw()
#circle1.show()

spectrum = spec.Spectrum(1)
spectrum.draw()
spectrum.show()