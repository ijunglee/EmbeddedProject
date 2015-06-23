import sys
import desktop
from desktop import Ui_MainWindow
from PyQt4.QtGui import QMainWindow
from PyQt4 import QtCore, QtGui
 
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
 
if __name__ == '__main__':
    app = desktop.QtGui.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
