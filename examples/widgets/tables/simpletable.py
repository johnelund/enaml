#------------------------------------------------------------------------------
#  Copyright (c) 2013, Nucleic Development Team.
#  All rights reserved.
#------------------------------------------------------------------------------
#from atom.api import Atom, Str, Range, Bool, observe

import enaml
from enaml.qt.qt_application import QtApplication

if __name__ == '__main__':
    with enaml.imports():
        from simpletable import SimpleTableView

    app = QtApplication()
    view = SimpleTableView()
    view.show()

    app.start()
