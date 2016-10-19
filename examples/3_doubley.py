import matplotlib.pyplot as plt
from pubplots import PlotData
import pubplots.plot as pbt

# This file shows a plot with a scatter to the right hand axes


reddata = PlotData()
reddata.onefile('data/reduction.txt', xcol=0, ycols=[2], yrcols=[1],
                xaxislabel='Time [s]', yaxislabel='Temperature [$^\circ$C]',
                yraxislabel='Pressure [Pa]')

# Supose we want lines plotted to the left and markers to the right
# And no grid
fig = plt.figure(figsize=(8, 6), facecolor='white')
ax = plt.subplot(111)
axr = pbt.quick_modern(ax, reddata, rscatter=True, grid=False)
ax.set_xlim(0,55)
pbt.save('3_reduction')
plt.show()

# Plot 2
oxdata = PlotData()
oxdata.onefile('data/oxidation.txt', xcol=0, ycols=[2], yrcols=[1], xaxislabel='Time [s]',
               yaxislabel='Temperature [$^\circ$C]', yraxislabel='Pressure [Pa]')

# Make an old style graph
fig = plt.figure(figsize=(8, 6), facecolor='white')
ax = plt.subplot(111)
axr = pbt.quick_modern(ax, oxdata, rscatter=True, grid=False)
ax.set_xlim(0,155)
pbt.save('3_oxidation')
plt.show()
