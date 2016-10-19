"""A set of scripts for producing nice plots using matplotlib,
Made to be used in combination with the class PlotData, which contains methods
for selecting the data from csv files and assiging axes labels and data labels.

Note this is not a wrapper to replace matplolib, it is just a set of scripts
which take matplotlib axes objects and make nicer plots than the default matplotlib ones.
"""
import os
import math
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle
from pubplots.colorsmarkers import pubcolors, pubmarkers, publs, pubdashes, TB10


def set_colors(colors):
    """Take a key and set the colors accordingly, or return the same list if a list is passed

    Parameters
    ----------
    colors : str or list of (r,g,b) tupples
        Pass a string options are 'black', 'grey', 'tb10', 'tb20' and 'cb10'(for colorblind people)

    Returns
    -------
    list of tupples
        A list of (r,g,b) tuples
    """
    try:
        return pubcolors[colors]
    except KeyError:
        print('Not a valid color key, options: ', pubcolors.keys())
        print('Using default tb10 instead')
        return pubcolors['tb10']
    except TypeError:
        if type(colors).__name__ == 'list':
            return colors
        else:
            raise


def set_linestyles(linestyles):
    """return a list of linestyles or unchanged list if a list is passed

    Parameters
    ----------
    linestyles : str or list
        options '-' or '--', '..' or, '.-' or a list with variations of these

    Returns
    -------
    list
        passed list or makes a list from '-'
    """
    try:
        return publs[linestyles]
    except KeyError:
        print('Not a valid linestyle key, options: ', publs.keys())
        print('Using default - instead')
        return publs['-']
    except TypeError:
        if type(linestyles).__name__ == 'list':
            return linestyles
        else:
            raise


def set_markers(markers):
    """return a list of markers if a str key is passed

    Parameters
    ----------
    markers : str or list
        'var' gives a list of varying markers

    Returns
    -------
    list
        list of markers

    """
    try:
        return pubmarkers[markers]
    except KeyError:
        print('Not a valid markers key, options: ', pubmarkers.keys())
        print('Using default var instead')
        return pubmarkers['var']
    except TypeError:
        if type(markers).__name__ == 'list':
            return markers
            pass
        else:
            raise


def axis_labels(ax,  xaxislabel='x', yaxislabel='y', title=None, fontsize=20):
    """Lable the x a nd y axis and optionally add a title.

    Parameters
    ----------
    ax : matplotlib.axes object
        this is the maplotlib axes to be labeled
    xaxislabel : str, optional
    yaxislabel : str, optional
    title : None, optional
        add title str if you want a title
    fontsize : int, optional
    """
    ax.set_xlabel(xaxislabel, fontsize=fontsize)
    ax.set_ylabel(yaxislabel, fontsize=fontsize)
    if title is not None:
        ax.set_title(title, fontsize=fontsize, loc='left', y=1.08)


def remove_boundary(ax):
    """Remove the spines. Common in modern presentation graphs

    Parameters
    ----------
    ax : matplotlib.axes object
        the axes to to have the spines remoced
    """
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_visible(False)


def remove_right_top(ax):
    """Remove top and right boundaries

    Parameters
    ----------
    ax : matplotlib.axes object
        the axes to to have the spines remoced
    """
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)


def modern_style(ax, fontsize=18, grid=True):
    """modern style. No boundary and y-grid. ticks on left and bottom

    Parameters
    ----------
    ax : matplotlib.axes object
    fontsize : int, optional
    grid : bool, optional
    """
    remove_boundary(ax)
    ax.tick_params(axis="both", which="both", bottom="on", top="off", labelbottom="on",
                   left="on", right="off", labelleft="on", labelsize=18, width=2.5)
    if grid:
        ax.grid(grid, linestyle='--', axis='y', color='0.60')


def semi_modern_style(ax, fontsize=18, grid=True):
    """Bottom and left boundarys. y-grid nicetableau colors

    Parameters
    ----------
    ax : matplotlib.axes object
    fontsize : int, optional
    grid : bool, optional
    """
    remove_right_top(ax)
    ax.tick_params(axis="both", which="both", bottom="on", top="off",
                   labelbottom="on", left="on", right="off", labelleft="on",
                   labelsize=fontsize, width=2)
    if grid:
        ax.grid(grid, linestyle='--', axis='y', color='0.60')


def old_hat_style(ax, fontsize=18):
    """Typical graph style. Bounding box. Black lines

    Parameters
    ----------
    ax : matplotlib.axes object
    fontsize : int, optional
    """
    ax.tick_params(axis="both", which="both", bottom="on", top="off",
                   labelbottom="on", left="on", right="off",
                   labelsize=fontsize, labelleft="on", width=2)


def plot_lines(ax, yset, lw=2.0, dashes=None, linestyles='-', colors='tb10', **kwargs):
    """plot passed data as lines. Note it uses a ziped set  of lists so the shortest
    list is the maximum number of plots. TB10 just has 10 colors so it will plot a maximum of 10
    lines. For more use 'tb20'

    Parameters
    ----------
    ax : matplotlib.axes object
    yset : list
        list of data to plot like[[x1array, y1array], [x2array, y2array].....].
        x1,y1 are arrays or lists of numbers for plotting
    lw : float, optional
        linewidth
    dashes : None, Bool or list, optional
        True turns on varying dasshes. or list like [[7,3],[9,3,2,3]...] of dash specifications
        can be passed. line.set_dashes from matplotlib
    linestyles : str or list, optional
        '-' for continuous lines '--' dashed
    colors : str or list of (r,g,b) tupples
        Pass a string options are 'black', 'grey', 'tb10', 'tb20' and 'cb10'(for colorblind people)
    **kwargs : TYPE
        passed to matplotlib axes.plot()
    """
    if dashes is True:
        dashes=pubdashes
    colors=set_colors(colors)
    linestyles=set_linestyles(linestyles)
    i=0
    for data, ls, color in zip(yset, linestyles, colors):
        # PLot the dataa
        a, = ax.plot(data[0], data[1], ls, color=color, lw=lw, **kwargs)
        if dashes and i>0:
            a.set_dashes(dashes[i])
        i=i+1


def plot_scatter(ax, yset, markersize=10, fillstyle='full',
                 markers='var', markeredgewidth=0.0, colors='tb10'):
    """plot passed data as a scatter plot. Note it uses a ziped set of lists so the shortest
    list is the maximum number of plots. For example colors is currently of length ten.

    Parameters
    ----------
    ax : matplotlib.axes object
    yset : list
        list of data to plot like[[x1array, y1array], [x2array, y2array].....].
        x1,y1 are arrays or pointers to arrays/lists of numbers
    markersize : int, optional, default 10
    fillstyle : str, optional, default 'full'
    markers : str or list of matplotlib markers e.g. ['o','s']
        default is 'var' which is a list of matplotlib markers
    markeredgewidth : float, optional, default 0.0
    colors : str or list of (r,g,b) tupples
        Pass a string options are 'black', 'grey', 'tb10', 'tb20' and 'cb10'(for colorblind people)

    """
    colors=set_colors(colors)
    markers=set_markers(markers)
    for data, marker, color in zip(yset, markers, colors):
        # PLot the data
        ax.plot(data[0], data[1], linestyle='none', marker=marker,
            fillstyle=fillstyle, color=color, markersize=markersize,
            markeredgewidth=markeredgewidth)


def plot_lright(ax, yset, lw=2.0, yaxlabel='y2', linestyles='-',
                color=TB10[0], fontsize=18, spine=False, **kwargs):
    """plot line to right hand axis. Also colors the right hand labels to of the line and returns
    The right hand axis. By default it is the tableau blue color

    Parameters
    ----------
    ax : matplotlib.axes object
    yset : list
        list of data to plot like[[x1array, y1array], [x2array, y2array].....].
        x1,y1 are arrays or pointers to arrays/lists of numbers
    lw : float, optional
        linewidth
    yaxlabel : str, optional
        Label to be added to the right hand y axis
    linestyles : str or list, optional
        '-' for continuous lines '--' dashed
    color : (r,g,b) tupple, or matplotlib color 'b'- blue
    fontsize : int, optional
    spine : bool, optional
        True - Include the right hand frame spine
    **kwargs : TYPE
        passed to matplotlib axes.plot()


    Returns
    ----------
    matplotlib.axes object
        returns the new right hand axes
    """
    ax.set_zorder(1)
    ax.patch.set_visible(False)
    linestyles=set_linestyles(linestyles)
    axr = ax.twinx()
    axr.set_frame_on(True)
    axr.spines["right"].set_edgecolor(color)
    axr.patch.set_visible(False)
    axr.spines["top"].set_visible(False)
    axr.spines["bottom"].set_visible(False)
    axr.spines["right"].set_visible(spine)
    axr.spines["left"].set_visible(False)
    for data, ls in zip(yset, linestyles):
        # PLot the data
        axr.plot(data[0], data[1], ls, color=color, lw=lw, **kwargs)
    for tl in axr.get_yticklabels():
        # Color the tick labels
        tl.set_color(color)
    axr.set_ylabel(yaxlabel, color=color, fontsize=20)
    axr.tick_params(axis='both', which='major', labelsize=fontsize, width=2.5,color=color)
    return axr


def plot_lright2(ax, yset, lw=2.0, yaxlabel='None', color=TB10[3],
                 fontsize=18, linestyles='-', spine=False,**kwargs):
    """plot line to displaced right hand axis and returns the axis.
    Also colors the right hand labels to that if the
    line. By default it is the tableau red color

    Parameters
    ----------
    ax : matplotlib.axes object
    yset : list
        list of data to plot like[[x1array, y1array], [x2array, y2array].....].
        x1,y1 are arrays or pointers to arrays/lists of numbers
    lw : float, optional
        linewidth
    yaxlabel : str, optional
        Label to be added to the right hand y axis
    linestyles : str or list, optional
        '-' for continuous lines '--' dashed
    color : (r,g,b) tupple, or matplotlib color 'b'- blue
    fontsize : int, optional
    spine : bool, optional
        True - Include the right hand frame spine
    **kwargs : TYPE
        passed to matplotlib axes.plot()

    Returns
    ----------
    matplotlib.axes object
        returns the new right hand axes
    """
    linestyles=set_linestyles(linestyles)
    axr2 = ax.twinx()
    axr2.set_frame_on(True)
    axr2.patch.set_visible(False)
    axr2.spines["right"].set_edgecolor(color)
    axr2.spines["top"].set_visible(False)
    axr2.spines["bottom"].set_visible(False)
    axr2.spines["right"].set_visible(spine)
    axr2.spines["left"].set_visible(False)
    axr2.spines["right"].set_position(("outward", 100))
    for data, ls in zip(yset, linestyles):
        # PLot the data
        axr2.plot(data[0], data[1], ls, color=color, lw=lw, **kwargs)
    for tl in axr2.get_yticklabels():
        # Color the tick labels
        tl.set_color(color)
    axr2.set_ylabel(yaxlabel, color=color, fontsize=20)
    axr2.tick_params(axis='both', which='major', labelsize=fontsize, width=2.5, color=color)
    return axr2


def plot_sright(ax, yset, markersize=8, fillstyle='full', markers='var', yaxlabel='y2',
                color=TB10[0], fontsize=18, markeredgewidth=0.0, spine=False,
                **kwargs):
    """plot scatter to right hand axis. Also colors the right hand labels to that if the line. By
    default it is the tableau blue color

    Parameters
    ----------
    ax : matplotlib.axes object
    yset : list
        list of data to plot like[[x1array, y1array], [x2array, y2array].....].
        x1,y1 are arrays or pointers to arrays/lists of numbers
    markersize : int, optional, default 10
    fillstyle : str, optional, default 'full'
    markers : str or list of matplotlib markers e.g. ['o','s']
        default is 'var' which is a list of matplotlib markers
    markeredgewidth : float, optional, default 0.0
    yaxlabel : str, optional
        Label to be added to the right hand y axis
    color : (r,g,b) tupple, or matplotlib color 'b'- blue
    fontsize : int, optional
    spine : bool, optional
        True - Include the right hand frame spine
    **kwargs : TYPE
        passed to matplotlib axes.plot()

    Returns
    ----------
    matplotlib.axes object
        returns the new right hand axes
    """
    ax.set_zorder(1)
    ax.patch.set_visible(False)
    markers=set_markers(markers)
    axr = ax.twinx()
    axr.set_frame_on(True)
    axr.patch.set_visible(False)
    axr.spines["right"].set_edgecolor(color)
    axr.spines["top"].set_visible(False)
    axr.spines["bottom"].set_visible(False)
    axr.spines["right"].set_visible(spine)
    axr.spines["left"].set_visible(False)
    for data, marker in zip(yset, markers):
        # PLot the data
        axr.plot(data[0], data[1], linestyle='None', fillstyle=fillstyle, marker=marker,
                 color=color, markersize=markersize, markeredgewidth=markeredgewidth, **kwargs)
    axr.set_ylabel(yaxlabel, color=color, fontsize=24)
    for tl in axr.get_yticklabels():
        tl.set_color(color)
    axr.tick_params(axis="both", which="both", bottom="on", top="off", labelbottom="on",
                    left="off", right="off", labelleft="off", width=2,
                    labelsize=fontsize, color=color)
    ax.tick_params(axis="both", which="both", bottom="on", top="off",
                   labelbottom="on", left="off", right="off", labelleft="on", width=2)
    return axr


def plot_sright2(ax , yset, markersize=8, fillstyle='full', markers='var', yaxlabel='y3',
                 color=TB10[3], fontsize=18, markeredgewidth=0.0, spine=False,
                 **kwargs):
    """plot scatter to right hand axis. Also colors the right hand labels to that if the line. By
    default it is the tableau blue color

    Parameters
    ----------
    ax : matplotlib.axes object
    yset : list
        list of data to plot like[[x1array, y1array], [x2array, y2array].....].
        x1,y1 are arrays or pointers to arrays/lists of numbers
    markersize : int, optional, default 10
    fillstyle : str, optional, default 'full'
    markers : str or list of matplotlib markers e.g. ['o','s']
        default is 'var' which is a list of matplotlib markers
    markeredgewidth : float, optional, default 0.0
    yaxlabel : str, optional
        Label to be added to the right hand y axis
    color : (r,g,b) tupple, or matplotlib color 'b'- blue
    fontsize : int, optional
    spine : bool, optional
        True - Include the right hand frame spine
    **kwargs : TYPEV
        passed to matplotlib axes.plot()

    Returns
    ----------
    matplotlib.axes object
        returns the new right hand axes
    """
    markers=set_markers(markers)
    axr2 = ax.twinx()
    axr2.set_frame_on(True)
    axr2.patch.set_visible(False)
    axr2.spines["right"].set_edgecolor(color)
    axr2.spines["top"].set_visible(False)
    axr2.spines["bottom"].set_visible(False)
    axr2.spines["right"].set_visible(spine)
    axr2.spines["left"].set_visible(False)
    axr2.spines["right"].set_position(("outward", 100))
    for data, marker in zip(yset, markers):
        # PLot the data
        axr2.plot(data[0], data[1], linestyle='None', fillstyle=fillstyle, marker=marker,
                  color=color, markersize=markersize, markeredgewidth=markeredgewidth, **kwargs)
    axr2.set_ylabel(yaxlabel, color=color, fontsize=24)
    for tl in axr.get_yticklabels():
        tl.set_color(color)
    axr2.tick_params(axis="both", which="both", bottom="on", top="off", labelbottom="on",
                     left="off", right="off", labelleft="off", width=2,
                     labelsize=fontsize, color=color)
    ax.tick_params(axis="both", which="both", bottom="on", top="off",
                   labelbottom="on", left="off", right="off", labelleft="on", width=2)
    return axr2


def inset_plot(fig, ax, yset, lbwh=[0.58,0.58,0.40,0.40], grid=False, dashes=None,
               xlabel=None, ylabel=None, title=None, fontsize=14, colors='tb10', style='modern',
               scatter=False, label=False, labels=[], at_x=None, linestyles='-', markers='var',
               **kwargs):
    """Make an inset plot positioned in the top right

    Parameters
    ----------
    fig : matplotlib.figure object
        The figure to add the inset to
    ax : matplotlib.axes object
    yset : list
        list of data to plot like[[x1array, y1array], [x2array, y2array].....].
        x1,y1 are arrays or pointers to arrays/lists of numbers
    lbwh : list, optional
        [l,b,w,h], l, b is where to place the inset and w, h is its size
    grid : bool, optional
        add a grid, default False
    dashes : None, optional
        True - adds carying dashes
    xlabel : None or str, optional
        str to add to the xaxis label
    ylabel : None or str, optional
        string fro yaxis label
    title : None or str, optionl
        string for inset title
    fontsize : int, optional
    colors : str or list of (r,g,b) tupples
        Pass a string options are 'black', 'grey', 'tb10', 'tb20' and 'cb10'(for colorblind people)
    style : str, optional
        one of 'modern', 'semimodern' or 'oldhat'
    scatter : bool, optional
        use markers instead of lines
    label : bool, optional
        label the lines
    labels : list, optional
        list of labels
    at_x : None or list, optional
        list of x co-cordinates to align the labels with
    linestyles : TYPE, optional
    markers : str, optional
    **kwargs : TYPEV
        passed to matplotlib axes.plot()

    Returns
    ----------
    matplotlib.axes object
        returns the new right hand axes
    """
    colors=set_colors(colors)
    linestyles=set_linestyles(linestyles)
    markers=set_markers(markers)
    rect = Rectangle((lbwh[2]+0.07,lbwh[3]+0.04), lbwh[0]-0.03, lbwh[1]-0.03,
                     facecolor='white', edgecolor='black', transform=fig.transFigure,
                     zorder=1)
    fig.patches.append(rect)
    axin = fig.add_axes(lbwh, zorder=2)
    if ylabel is not None:
        axin.set_xlabel(xlabel, fontsize=fontsize)
    if ylabel is not None:
        axin.set_ylabel(ylabel, fontsize=fontsize)
    if title is not None:
        axin.set_title(title, fontsize=fontsize, loc='left', y=1.08)
    if style=='modern':
        modern_style(axin, fontsize=fontsize, grid=grid)
    elif style=='semimodern':
        semi_modern_style(axin, fontsize=fontsize, grid=grid)
    elif style=='oldhat':
        semi_modern_style(axin, fontsize=fontsize)
    else:
        print('Incorrect style options are: "modern", "semimodern" and "oldhat"')
    if scatter:
        plot_scatter(axin, yset, markers= markers,
                     markersize=6, markeredgewidth=1.5, colors=colors, **kwargs)
    else:
        plot_lines(axin, yset, lw=1.5, dashes=dashes, linestyles=linestyles, **kwargs)
    if label is True:
        label_lines(axin, yset, at_x=at_x, labels=labels, colors=colors, fontsize=fontsize-2)
    return axin


def add_yerrors(ax, yset=None, errors=None, colors='tb10', elinewidth=1.5):
    """Add x or y or both error bars to the plot

    Parameters
    ----------
    ax : matplotlib.axes object
    yset : list
        list of data to plot like[[x1array, y1array], [x2array, y2array].....].
        x1,y1 are arrays or lists of numbers for plotting
    errors : list
        list of yerrors to go with each data set in yset
    colors : str or list of (r,g,b) tupples
        Pass a string options are 'black', 'grey', 'tb10', 'tb20' and 'cb10'(for colorblind people)
    elinewidth : float, optional
    """
    for data, error, color in zip(plotdata, errors, colors):
        # Add error bars
        ax.errorbar(data[0], data[1], yerr=error, fmt='None',
                    ecolor=color, elinewidth=elinewidth)
        # Adding labels to the lines


def label_lines(ax, yset, at_x=None,
                rotation_on=False,
                labels=[], offsets=[(0, 0)]*10, colors='tb10', fontsize=18):
    """Add in graph labels, which are often much better than having a legend. Uses np.interpolate
    together with the yset's to place the label

    Parameters
    ----------
    ax : matplotlib.axes object
    yset : list
        list of data to plot like[[x1array, y1array], [x2array, y2array].....].
        x1,y1 are arrays or lists of numbers for plotting
    at_x : None or list, optional
        list of x co-cordinates to align the labels with
    rotation_on : bool, optional
        rotate the labels inline with the plotted data
    labels : list, optional
        list of labels
    offsets : TYPE, optional
        list of offsets to move the data from the intial placement point
    colors : str or list of (r,g,b) tupples
        Pass a string options are 'black', 'grey', 'tb10', 'tb20' and 'cb10'(for colorblind people)
    fontsize : int, optional
    """
    colors=set_colors(colors)
    if at_x is None:
        at_x = []
        for i, data in enumerate(yset):
            at_x.append(data[0].min()+(i+1)*(data[0].max()-data[0].min())/(len(yset)+1))
        for data, x, color, label, offset in zip(yset, at_x, colors, labels, offsets):
            label_line(ax, data[0], data[1], label, color,
                       at_x=x,
                       rotation_on=rotation_on, fontsize=fontsize, offset=offset)
    else:
        for data, x, color, label, offset in zip(yset, at_x, colors, labels, offsets):
            label_line(ax, data[0], data[1], label, color,
                       at_x=x,
                       rotation_on=rotation_on, fontsize=fontsize, offset=offset)


def quick_modern(ax, plotdata, figsize=(9, 6), scatter=False, rscatter=False, grid=True,
                  r2scatter=False, at_x=None, label=True, fontsize=18):
    """Make a modern style plot from a PlotData object

    Parameters
    ----------
    ax : matplotlib.axes object
    plotdata : PlotData object see plotdata from pubplots.
        Holds the information of what data to plot and axislabels line labels etc.
    figsize : tuple, optional
        (9,6) is the default
    scatter : bool, optional
        True use markers instead of lines
    rscatter : bool, optional
        USe markers instead of lines on the right hand axes
    grid : bool, optional
        Turn on grid for primerary axes
    r2scatter : bool, optional
        USe markers instead of lines on the right hand axes
    at_x : None, optional
        list of x_positions for the labels on the primerary axes
    label : bool, optional
        True labels the lines
    fontsize : int, optional

    Returns
    ----------
    r1,r2 : matplotlib.axes objects
        returns the new right hand axes, None, None if nothing is plotted to the right hand axes
    """
    modern_style(ax, fontsize=fontsize, grid=grid)
    axis_labels(ax, plotdata.xaxislabel, plotdata.yaxislabel, fontsize=fontsize+int(fontsize/9))
    r1 = None
    r2 = None
    if plotdata.yr2set==[] and 1<len(plotdata.yset)<6:
        # Make a colorfule plot using tb5, any right axes data is plotted grey
        if scatter:
            plot_scatter(ax, plotdata.yset, colors='tb5')
        else:
            plot_lines(ax, plotdata.yset, colors='tb5')
        if label is True:
            label_lines(ax, plotdata.yset, at_x=at_x, labels=plotdata.labels, colors='tb5')
        if plotdata.yrset!=[]:
            if rscatter:
                r1 = plot_sright(ax, plotdata.yrset,
                                    yaxlabel=plotdata.yraxislabel, color=(0.36,0.36,0.39))
            else:
                r1 = plot_lright(ax, plotdata.yrset,
                    yaxlabel=plotdata.yraxislabel, color=(0.36,0.36,0.39))
            if label is True:
                label_lines(r1, plotdata.yrset, labels=plotdata.yrlabels, colors=[(0.36,0.36,0.39)]*20)
    elif plotdata.yrset != []:
        # if we have right axes data make a plot where all left axes data is black
        # and right axes data is blue from tb10
        if scatter:
            plot_scatter(ax, plotdata.yset, colors='black')
        else:
            plot_lines(ax, plotdata.yset, colors='black')
        if label is True:
            label_lines(ax, plotdata.yset, at_x=at_x, labels=plotdata.labels, colors='black')
        if rscatter:
            r1 = plot_sright(ax, plotdata.yrset,
                yaxlabel=plotdata.yraxislabel)
        else:
            r1 = plot_lright(ax, plotdata.yrset,
                yaxlabel=plotdata.yraxislabel)
        if label is True:
            label_lines(r1, plotdata.yrset, labels=plotdata.yrlabels, colors=[TB10[0]]*20)
    elif len(plotdata.yset) > 10:
        if scatter:
            plot_scatter(ax, plotdata.yset, colors='tb20')
        else:
            plot_lines(ax, plotdata.yset, colors='tb20')
        if label is True:
            label_lines(ax, plotdata.yset, at_x=at_x, labels=plotdata.labels, colors='tb20')
    else:
        if scatter:
            plot_scatter(ax, plotdata.yset)
        else:
            plot_lines(ax, plotdata.yset)
        if label is True:
            label_lines(ax, plotdata.yset, at_x=at_x, labels=plotdata.labels)
    if plotdata.yr2set != []:
        if r2scatter:
            r2 = plot_sright2(ax, plotdata.yr2set,
                yaxlabel=plotdata.yr2axislabel)
        else:
            r2 = plot_lright2(ax,plotdata.yr2set,
                yaxlabel=plotdata.yr2axislabel)
        if label is True:
            label_lines(r2, plotdata.yr2set, labels=plotdata.yr2labels, colors=[TB10[3]]*20)
    return r1, r2


def quick_semimodern(ax, plotdata, figsize=(9, 6), scatter=False, rscatter=False, grid=True,
                  r2scatter=False, at_x=None, label=True, fontsize=18):
    """Make a modern style plot from a PlotData object

    Parameters
    ----------
    ax : matplotlib.axes object
    plotdata : PlotData object see plotdata from pubplots.
        Holds the information of what data to plot and axislabels line labels etc.
    figsize : tuple, optional
        (9,6) is the default
    scatter : bool, optional
        True use markers instead of lines
    rscatter : bool, optional
        USe markers instead of lines on the right hand axes
    grid : bool, optional
        Turn on grid for primerary axes
    r2scatter : bool, optional
        USe markers instead of lines on the right hand axes
    at_x : None, optional
        list of x_positions for the labels on the primerary axes
    label : bool, optional
        True labels the lines
    fontsize : int, optional

    Returns
    ----------
    r1,r2 : matplotlib.axes objects
        returns the new right hand axes, None, None if nothing is plotted to the right hand axes
    """
    axis_labels(ax, plotdata.xaxislabel, plotdata.yaxislabel, fontsize=fontsize+int(fontsize/9))
    semi_modern_style(ax, fontsize=fontsize, grid=grid)
    r1 = None
    r2 = None
    if plotdata.yr2set==[] and 1<len(plotdata.yset)<6:
        # Make a colorfule plot using tb5, any right axes data is plotted grey
        if scatter:
            plot_scatter(ax, plotdata.yset, colors='tb5')
        else:
            plot_lines(ax, plotdata.yset, colors='tb5')
        if label is True:
            label_lines(ax, plotdata.yset, at_x=at_x, labels=plotdata.labels, colors='tb5')
        if plotdata.yrset!=[]:
            if rscatter:
                r1 = plot_sright(ax, plotdata.yrset, spine=True,
                                    yaxlabel=plotdata.yraxislabel, color=(0.36,0.36,0.39))
            else:
                r1 = plot_lright(ax, plotdata.yrset, spine=True,
                    yaxlabel=plotdata.yraxislabel, color=(0.36,0.36,0.39))
            if label is True:
                label_lines(r1, plotdata.yrset, labels=plotdata.yrlabels, colors=[(0.36,0.36,0.39)]*20)
    elif plotdata.yrset != []:
        if scatter:
            plot_scatter(ax, plotdata.yset, colors='black')
        else:
            plot_lines(ax, plotdata.yset, colors='black')
        if label is True:
            label_lines(ax, plotdata.yset, at_x=at_x, labels=plotdata.labels, colors='black')
        if rscatter:
            r1 = plot_sright(ax, plotdata.yrset,
                yaxlabel=plotdata.yraxislabel, spine=True)
        else:
            r1 = plot_lright(ax, plotdata.yrset,
                yaxlabel=plotdata.yraxislabel, spine=True)
        if label is True:
            label_lines(r1, plotdata.yrset, labels=plotdata.yrlabels, colors=[TB10[0]]*20)
    elif len(plotdata.yset) > 10:
        if scatter:
            plot_scatter(ax, plotdata.yset, colors='tb20')
        else:
            plot_lines(ax, plotdata.yset, colors='tb20')
        if label is True:
            label_lines(ax, plotdata.yset, at_x=at_x, labels=plotdata.labels, colors='tb20')
    else:
        if scatter:
            plot_scatter(ax, plotdata.yset)
        else:
            plot_lines(ax, plotdata.yset)
        if label is True:
            label_lines(ax, plotdata.yset, at_x=at_x, labels=plotdata.labels)
    if plotdata.yr2set != []:
        if r2scatter:
            r2 = plot_sright2(ax, plotdata.yr2set,
                yaxlabel=plotdata.yr2axislabel, spine=True)
        else:
            r2 = plot_lright2(ax,plotdata.yr2set,
                yaxlabel=plotdata.yr2axislabel, spine=True)
        if label is True:
            label_lines(r2, plotdata.yr2set, labels=plotdata.yr2labels, colors=[TB10[3]]*20)
    return r1, r2


def quick_old_hat(ax, plotdata, figsize=(9, 6), scatter=False, rscatter=False,
                  r2scatter=False, at_x=None, label=True, fontsize=18, dashes=False):
    """Make a modern style plot from a PlotData object

    Parameters
    ----------
    ax : matplotlib.axes object
    plotdata : PlotData object see plotdata from pubplots.
        Holds the information of what data to plot and axislabels line labels etc.
    figsize : tuple, optional
        (9,6) is the default
    scatter : bool, optional
        True use markers instead of lines
    rscatter : bool, optional
        USe markers instead of lines on the right hand axes
    grid : bool, optional
        Turn on grid for primerary axes
    r2scatter : bool, optional
        USe markers instead of lines on the right hand axes
    at_x : None, optional
        list of x_positions for the labels on the primerary axes
    label : bool, optional
        True labels the lines
    fontsize : int, optional
    dashes : None, optional
        True - adds varying dashes

    Returns
    ----------
    r1,r2 : matplotlib.axes objects
        returns the new right hand axes, None, None if nothing is plotted to the right hand axes
    """
    old_hat_style(ax, fontsize=fontsize)
    axis_labels(ax, plotdata.xaxislabel, plotdata.yaxislabel, fontsize=fontsize+int(fontsize/9))
    r1 = None
    r2 = None
    if plotdata.yrset != []:
        if scatter:
            plot_scatter(ax, plotdata.yset, colors='black')
        else:
            plot_lines(ax, plotdata.yset, colors='black', dashes=dashes)
        if label is True:
            label_lines(ax, plotdata.yset, at_x=at_x, labels=plotdata.labels, colors='black')
        if rscatter:
            r1 = plot_sright(ax, plotdata.yrset,
                yaxlabel=plotdata.yraxislabel, spine=True, color=(0.35,0.35,0.39))
        else:
            r1 = plot_lright(ax, plotdata.yrset,
                yaxlabel=plotdata.yraxislabel, spine=True, color=(0.35,0.35,0.39))
        if label is True:
            label_lines(r1, plotdata.yrset, labels=plotdata.yrlabels, colors=[(0.35,0.35,0.39)]*20)
    else:
        if scatter:
            plot_scatter(ax, plotdata.yset, colors='black')
        else:
            plot_lines(ax, plotdata.yset, dashes=dashes, colors='black')
        if label is True:
            label_lines(ax, plotdata.yset, at_x=at_x, labels=plotdata.labels, colors='black')
    if plotdata.yr2set != []:
        if r2scatter:
            r2 = plot_sright2(ax, plotdata.yr2set,
                yaxlabel=plotdata.yr2axislabel,
                color=(0.65,0.55,0.55), spine=True)
        else:
            r2 = plot_lright2(ax,plotdata.yr2set,
                yaxlabel=plotdata.yr2axislabel,
                color=(0.65,0.55,0.55), spine=True)
        if label is True:
            label_lines(r2, plotdata.yr2set, labels=plotdata.yr2labels, colors=[(0.59,0.59,0.5)]*20)
    return r1, r2


def save(name='plot'):
    """save as png and pdf

    Parameters
    ----------
    name : str, optional
        file name
    """
    if not os.path.exists("plots"):
        os.makedirs("plots")
    plt.savefig(os.path.join('plots', name + '.png'), dpi=150, bbox_inches='tight')
    plt.savefig(os.path.join('plots', name + '.pdf'), dpi=150, bbox_inches='tight')
    plt.tight_layout()


def label_line(ax, x, y, label_text, color,
               at_x=0,
               rotation_on=False,
               fontsize=14,
               offset=(0, 0)):
    """This Function allows to put labels onto a line graph. the labesl land on the line by
    by default. The can be set to rotate to be inline with the line. roation_on = True. There
    can also be an ofset. It must also be passed an axis. Typically ax in my code.

    Parameters
    ----------
    ax : matplotlib.axes object
    x : array
        the xdata
    y : array
        the ydata
    label_text : str
    color : (r,g,b) tuple or standard matplotlib color
    at_x : int, optional
        x psoition for label
    rotation_on : bool, optional
    fontsize : int, optional
    offset : tuple, optional
        (x,y) offset from intial selected position
    """
    sat_x = at_x
    # Check for log scales
    if ax.get_xscale() == 'log':
        sx = np.log10(x)    # screen space
        sat_x = np.log10(at_x)
    else:
        sx = x
    if ax.get_yscale() == 'log':
        sy = np.log10(y)
    else:
        sy = y
    # place labels using numpy interpolation
    rotation = 0
    if rotation_on is True:
        dx = (sat_x+(ax.get_xlim()[1]-ax.get_xlim()[0])/20.0)/(ax.get_xlim()[1]-ax.get_xlim()[0])
        dy = np.interp(sat_x+dx, sx, sy)-np.interp(sat_x, sx, sy)
        rotation = 2*np.rad2deg(math.atan2(dy, dx))
    pos = [at_x+offset[0], np.interp(at_x, x, y)+offset[1]]
    plt.text(pos[0], pos[1], label_text, size=fontsize, rotation=rotation, color=color,
             ha="center", va="center", bbox=dict(ec='1', fc='1'))
