#------------------------------------------------------------------------------
# Copyright (c) 2013, Nucleic Development Team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file COPYING.txt, distributed with this software.
#------------------------------------------------------------------------------
from atom.api import Typed

from enaml.widgets.chaco_plot import ProxyChacoPlot

from .QtCore import Qt
from .QtGui import QFrame, QVBoxLayout

from .qt_control import QtControl


class QtChacoPlot(QtControl, ProxyChacoPlot):
    """ A Qt implementation of an Enaml ProxyChacoPlot.

    """
    #: A reference to the widget created by the proxy.
    widget = Typed(QFrame)

    #--------------------------------------------------------------------------
    # Initialization API
    #--------------------------------------------------------------------------
    def create_widget(self):
        """ Create the underlying widget.

        """
        widget = QFrame(self.parent_widget())
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        widget.setLayout(layout)
        self.widget = widget

    def init_layout(self):
        """ Initialize the layout of the underlying widget.

        """
        super(QtChacoPlot, self).init_layout()
        assert isinstance(self.widget, QFrame)
        container = self.declaration.container
        container.control.setParent(self.widget)
        self.widget.resize(800,800)
        self.relayout()

    #--------------------------------------------------------------------------
    # ProxyChacoPlot API
    #--------------------------------------------------------------------------
    def set_container(self, container):
        """ Set the Plot Window container for the widget.

        """
        print 'In set_container'
