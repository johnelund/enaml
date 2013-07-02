#------------------------------------------------------------------------------
# Copyright (c) 2013, Nucleic Development Team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file COPYING.txt, distributed with this software.
#------------------------------------------------------------------------------

from atom.api import (
    Bool, List, Typed, ForwardTyped, observe, set_default
)
from enaml.core.declarative import d_

from .control import Control, ProxyControl

class ProxyTableView(ProxyControl):
    #: A reference to the TableView declaration.
    declaration = ForwardTyped(lambda: TableView)

    def set_model(self, model):
        raise NotImplementedError

class TableView(Control):
    """ A view for tabular data.

    """

    #: Whether or not the vertical header is shown. Defaults to True.
    vertical_header_visible = d_(Bool(True))

    #: Whether or not the horizontal header is shown. Defaults to True.
    horizontal_header_visible = d_(Bool(True))

    model = d_(Typed(List))

    #: A scroll area is free to expand in width and height by default.
    hug_width = set_default('ignore')
    hug_height = set_default('ignore')

    #: A reference to the ProxyScrollArea object.
    proxy = Typed(ProxyTableView)
