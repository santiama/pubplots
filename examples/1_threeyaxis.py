import matplotlib.pyplot as plt
from pubplots import PlotData
import pubplots.plot as pbt

# Load up the data. This is tga data of the change in mass, the temperature and partial pressure
# vs. time. so we need 3 y-axis, with the data for each specified by ycol,
# yrcols (r stands for right y axis) and yr2cols.
# Plot data automatically uses the collumn headers from the first row as axis labels.
timedata = PlotData()
timedata.onefile('data/timedata.csv', xcol=0, ycols=[1], yrcols=[2], yr2cols=[3])


fig = plt.figure(figsize=(16, 6), facecolor='white')
ax = plt.subplot()
axr, axr2 = pbt.quick_semimodern(ax, timedata, label=False, fontsize=18)
# set po2 scale to log and adjust the left axis and the xaxis
axr2.set_yscale('log')
ax.set_xlim(0, 34.2)
ax.set_ylim(-4.2, 0.2)
# Saves as a pdf and a png in a folder/new folder 'plots', in the working directory
pbt.save('1_TGA_data_vs_time')
plt.show()
