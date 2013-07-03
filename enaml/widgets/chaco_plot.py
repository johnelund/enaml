#------------------------------------------------------------------------------
# Copyright (c) 2013, Nucleic Development Team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file COPYING.txt, distributed with this software.
#------------------------------------------------------------------------------
from atom.api import Typed, ForwardTyped, Bool, observe, set_default

from enaml.core.declarative import d_

from .control import Control, ProxyControl


#: Delay the import of enable until needed. This removes the hard
#: dependecy on enable for the rest of the Enaml code base.
def ChacoPlotContainer():
    from enable.api import Window
    return Window

class ProxyChacoPlot(ProxyControl):
    """ The abstract definition of a proxy ChacoPlot object.

    """
    #: A reference to the ChacoPlot declaration.
    declaration = ForwardTyped(lambda: ChacoPlot)

    def set_container(self, container):
        raise NotImplementedError


class ChacoPlot(Control):
    """ A control which can be used to embded a chaco plot.

    """
    #: The enable Window containing a Chaco plot to display in the widget.
    # This object *must* be an enable.api.Window
    # see examples/plots/chaco_plot.py for use
    container = d_(ForwardTyped(ChacoPlotContainer))

    #: hug settings
    hug_width = set_default('ignore')
    hug_height = set_default('ignore')

    #: A reference to the ProxyChacoPlot object.
    proxy = Typed(ProxyChacoPlot)

    #--------------------------------------------------------------------------
    # Observers
    #--------------------------------------------------------------------------
    @observe(('container')) # , 'toolbar_visible'))
    def _update_proxy(self, change):
        """ An observer which sends state change to the proxy.

        """
        # The superclass handler implementation is sufficient.
        super(ChacoPlot, self)._update_proxy(change)
