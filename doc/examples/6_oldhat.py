import matplotlib.pyplot as plt
from pubplots import PlotData
import pubplots.plot as pbt

# Data from FactSage for the thermal decomposition of H2O as a function of temperature
therm = PlotData()
therm.onefile('data/thermolysis.csv', xcol=1, ycols=[19, 4, 5, 6, 7, 9],
              yaxislabel='moles of species x')

# Old hat uses frames by default and black lines using dashes to distinguish them
fig = plt.figure(figsize=(8, 6), facecolor='white')
ax = plt.subplot()
pbt.quick_old_hat(ax, therm, at_x=[3000, 3800, 3470, 4000, 3600, 3000, 3000], dashes=True)
ax.set_xlim(2000, 5000)
ax.set_ylim(0, 1.0)
pbt.save('6_old_hat_thermolysis')
plt.show()
