import matplotlib.pyplot as plt
from matplotlib import rcParams
from pubplots import PlotData
import pubplots.plot as pbt

cont = PlotData()
cont.walkandfind('data', search='.xkcd', xcol=1, ycols=[0],
                 xaxislabel='Pressure [Bar]', yaxislabel='Temperature [K]')
plt.xkcd()

fig = plt.figure(figsize=(9,10),facecolor=('white'))
ax = plt.subplot()
pbt.modern_style(ax, fontsize=20, grid=False)
ax.set_xscale('log')
pbt.axis_labels(ax, 'Pressure [bar]', 'Temperature [K]', fontsize=24)
pbt.plot_lines(ax, cont.yset,colors='tb20')
pbt.plot_scatter(ax, cont.yset, markers='o', colors='tb20')
pbt.label_lines(ax, cont.yset, labels=cont.labels, colors='tb20', fontsize=18,
                at_x=[40, 110, 100, 110, 5e-7, 100, 5e-8,
                      90, 7e-8, 1e-1,80, 8e-8, 100, 5e-8, 5e-8, 5e-8],
                fontname='StayPuft')
ax.set_xlim(2e-8,1e2)
ax.set_ylim(450,2500)
pbt.save('8_with_xkcdmode')
plt.show()
