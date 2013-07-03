#------------------------------------------------------------------------------
#  Copyright (c) 2013, Nucleic Development Team.
#  All rights reserved.
#------------------------------------------------------------------------------
#from atom.api import Atom, Str, Range, Bool, observe

import os, sys
os.environ['ETS_TOOLKIT'] = 'qt4'

import enaml
from enaml.qt.qt_application import QtApplication

def make_plot():
    from numpy import linspace, pi, sin
    from enable.api import Component, Container, Window
    from chaco.api import create_line_plot, add_default_axes, add_default_grids, OverlayPlotContainer

    x = linspace(-pi,pi,100)
    y = sin(x)
    plot = create_line_plot((x,y))
    add_default_grids(plot)
    add_default_axes(plot)
    container = OverlayPlotContainer(padding = 50)
    container.add(plot)
    return Window(None, -1, component=container)

if __name__ == '__main__':
    with enaml.imports():
        from plot import SimplePlotView

    app = QtApplication()
    view = SimplePlotView(plot=make_plot(), initial_size=(620,500))
    view.show()

    app.start()
