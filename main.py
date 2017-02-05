from controllers.main_window_controller import *
from PyQt4 import QtGui
import sys
import ctypes

myappid = 'pablosuau.pybacklogger' 
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
        
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)

    main = MainWindowController()
    main.show()

    sys.exit(app.exec_())