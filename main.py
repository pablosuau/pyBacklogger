import sys
from controllers.main_window_controller import *
from PyQt5 import QtWidgets

def start_up_app():
    app = QtWidgets.QApplication(sys.argv)

    main = MainWindowController()
    main.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    start_up_app()
