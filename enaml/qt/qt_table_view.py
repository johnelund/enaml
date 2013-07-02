#------------------------------------------------------------------------------
# Copyright (c) 2013, Nucleic Development Team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file COPYING.txt, distributed with this software.
#------------------------------------------------------------------------------

from atom.api import Typed
from .QtCore import QRect, QVariant
from .QtGui import QTableView, QStandardItemModel, QStandardItem, QItemDelegate, QLineEdit
from enaml.widgets.table_view import ProxyTableView
from .qt_control import QtControl

class testDelegate(QItemDelegate):

    def __init__(self, parent, col_editor, ed_field, ed_args, *args, **kw):
        super(testDelegate, self).__init__(*args, **kw)
        self.editor_parent = parent
        self.col_editor = col_editor
        self.editor_field = ed_field
        self.editor_args = ed_args
        self.editor = None

    def createEditor(self,parent,option,index):
        if index.column() != 3:
            self.editor = QLineEdit(parent)
            return self.editor
        else:
            args = self.editor_args
            args['parent'] = self.editor_parent
            self.editor = self.col_editor(**self.editor_args)
            self.editor.show()
            return self.editor.proxy.widget

    def setModelData(self, editor, model, index):
        if index.column() != 3:
            model.setData(index,editor.text())
        else:
            model.setData(index,getattr(self.editor, self.editor_field, ''))


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

    def _cvt_model(self, model):
        mdl = None
        row_count = len(model)
        col_count = len(model[0].keys())
        col_names = {}
        mdl = QStandardItemModel(row_count, col_count, self.widget)

        for col, col_name in enumerate(sorted(model[0].keys())):
            mdl.setHorizontalHeaderItem(col, QStandardItem(col_name))
            col_names[col] = col_name

        for r in range(row_count):
            for c in range(col_count):
                mdl.setItem(r,c,QStandardItem(str(model[r][col_names[c]])))

        return mdl

    def init_widget(self):
        """ Initialize the underlying widget.

        """

        super(QtTableView, self).init_widget()
        d = self.declaration
        self.widget.setFrameRect(QRect(0, 0, 200,.10))
        self.set_vertical_header_visible(d.vertical_header_visible)
        self.set_horizontal_header_visible(d.horizontal_header_visible)
        delegate = testDelegate(d.col_editor_parent,
                                            d.col_editor,
                                            d.col_field,
                                            d.col_editor_args,
                                            self.widget)
        self.widget.setItemDelegate(delegate)
        self.set_model(d.model)

    def set_model(self, model):
        self.widget.setModel(self._cvt_model(model))

    def set_vertical_header_visible(self, visible):
        self.widget.verticalHeader().setVisible(visible)

    def set_horizontal_header_visible(self, visible):
        self.widget.horizontalHeader().setVisible(visible)
