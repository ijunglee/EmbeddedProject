import sys
import money_UI
from money_UI import Ui_MainWindow
from PyQt4.QtGui import QMainWindow
 
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
 
if __name__ == '__main__':
    app = money_UI.QtGui.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())