import sys
import matplotlib.pyplot as plt
from plotdata import PlotData
import plot as pbt

dg = PlotData()
dg.walkandfind(search='Delta', labels=['$p_\mathrm{O_2}=0.001$ [bar]', '1 bar', '6 bar'])


fig=plt.figure(figsize=(8,6))
ax=plt.subplot(111)
pbt.axis_labels(ax,'Temperature [K]', '$\Delta G$ [kJ mol$^{-1}$]')
pbt.old_hat_style(ax)
pbt.plot_lines(ax, dg.yset, colors='black')
ax.set_xlim((1010,1390))
ax.set_ylim((-60, 45))
#rotate the labels to the lines
pbt.label_lines(ax, dg.yset, at_x=[1200,1200,1200], labels=dg.labels, rotation_on=True, colors='black')
ax.axhline(y=0, color='k')
pbt.save('7_rotatedlabels')
plt.show()