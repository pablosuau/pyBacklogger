from controllers.main_window_controller import *
from PyQt5 import QtGui, QtWidgets
import sys
import ctypes

myappid = 'pablosuau.pybacklogger' 
#ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
        
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    main = MainWindowController()
    main.show()

    sys.exit(app.exec_())
