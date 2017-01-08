from controllers.main_window_controller import *
from PyQt4 import QtGui
import sys
        
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)

    main = MainWindowController()
    main.show()

    sys.exit(app.exec_())