import ross as rs
import numpy as np
import plotly.io as pio
import utils
import test
from ross.units import Q_

pio.renderers.default = "notebook"


# Material section

# from E and G_s
steel = rs.Material(name="Steel", rho=7810, E=210e9, Poisson=0.3)
steel.save_material()


bearing = rs.BearingElement(
    n=0, 
    kxx=np.array([0.5e6, 1.0e6, 2.5e6]),
    kyy=np.array([1.5e6, 2.0e6, 3.5e6]),
    cxx=np.array([0.5e3, 1.0e3, 1.5e3]),
    frequency=np.array([0, 1000, 2000]),
)

utils.Plot(bearing)



shaft_elem = [
    rs.ShaftElement(
        L=0.7,
        idl=2.0,
        odl=3.75,
        material=steel,
        shear_effects=True,
        rotary_inertia=True,
        gyroscopic=True,
    )
    for _ in range(6)
]

disk0 = rs.DiskElement.from_geometry(
    n=2, material=steel, width=0.07, i_d=2.0, o_d=3.75
)

disks = [disk0]

stfx = 1e6
stfy = 0.8e6

bearing0 = rs.BearingElement(0, kxx=stfx, kyy=stfy, cxx=0, n_link=7)
bearing1 = rs.BearingElement(6, kxx=stfx, kyy=stfy, cxx=0)
bearing2 = rs.BearingElement(7, kxx=stfx, kyy=stfy, cxx=0)

bearings = [bearing0, bearing1, bearing2]

pm0 = rs.PointMass(n=7, m=0.3)

pointmass = [pm0]

rotor1 = rs.Rotor(shaft_elem, disks, bearings,pointmass)


samples = 30

speed_range = np.linspace(300, 3000, samples)

campbell = rotor1.run_campbell(speed_range)

plot_campbell = campbell.plot(frequency_units="RPM",harmonics=[0.5,1])

test.plot_figure(plot_campbell)

