#------------------------------------------------------------------------------
# Copyright (c) 2013, Nucleic Development Team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file COPYING.txt, distributed with this software.
#------------------------------------------------------------------------------

from atom.api import Typed
from .QtGui import QTableView
from enaml.widgets.table_view import ProxyTableView
from .qt_control import QtControl


class QtTableView(QtControl, ProxyTableView):
    """ A Qt implementation of TableView.

    """
    #: A reference to the widget created by the proxy.
    widget = Typed(QTableView)

    #--------------------------------------------------------------------------
    # Initialization API
    #--------------------------------------------------------------------------
    def create_widget(self):
        """ Create the underlying tableview widget.

        """
        self.widget = QTableView(self.parent_widget())

    def init_widget(self):
        """ Initialize the underlying widget.

        """
        super(QtTableView, self).init_widget()
        d = self.declaration
