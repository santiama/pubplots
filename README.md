Pubplots quickly make nice publication quility plots from data stored in csv files.
=====================================================================================

Intended use
------------
Matplotlib is really great, but the standard format of plots are not very visually attractive. 
This liberary offers a set of scripts to be used alongside matplotlib, allowing visually
attractive plots to be quickly produced from csv files. It is not a wrapper replacing matplotlib.

It also includes a class for holding the plot data. This class has methods for loading data from csv files,
or preparing pandas DataFrames for plotting. These PlotData objects can then be passed to some quick plot methods 
to produce the plots.

A personla preference of mine is to use in graph labels as opposed to legends, so I didn't include
any legends in the scripts.

Documentation and examples
--------------------------
- [Examples](https://bulfinb.github.io/pubplots/pubplots#examples) are given in the documentation

- [Documentation](https://bulfinb.github.io/pubplots/pubplots)

See also
--------

If you are looking for a more feature rich matplotlib wrapper that makes attractive plots, check out 

- [seaborn](https://github.com/mwaskom/seaborn)

It is activly being maintained. 

I wrote these scripts before realising that seaborn existed. Having then come across it I 
decided to share them anyway.

credit
------

This package was partially inspired by [this blog
post](http://www.randalolson.com/2014/06/28/how-to-make-beautiful-data-visualizations-in-python-with-matplotlib/)

Dependencies
------------

- Python 2.7 or 3.3+

### Mandatory

- [numpy](http://www.numpy.org/)

- [matplotlib](http://matplotlib.sourceforge.net)

- [pandas](http://pandas.pydata.org/)

-------

Released under a BSD (3-clause) license
