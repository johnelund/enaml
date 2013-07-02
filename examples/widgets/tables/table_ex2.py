#------------------------------------------------------------------------------
#  Copyright (c) 2013, Nucleic Development Team.
#  All rights reserved.
#------------------------------------------------------------------------------
#from atom.api import Atom, Str, Range, Bool, observe

import enaml
from enaml.qt.qt_application import QtApplication

if __name__ == '__main__':
    with enaml.imports():
        from tableex2 import Ex2TableView

    app = QtApplication()
    view = Ex2TableView()
    view.show()

    app.start()
