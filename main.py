'''
Main entry point of the pyBacklogger application.
'''

import sys
from controllers.main_window_controller import MainWindowController
from PyQt5.QtWidgets import QApplication

def start_up_app():
    '''
    Launches the application's GUI.
    '''
    app = QApplication(sys.argv)

    main = MainWindowController()
    main.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    start_up_app()
