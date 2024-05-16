from pages import LoginForm, CreateAccountForm, HomePage
import sys
from PyQt5 import QtWidgets

class CookeryApp(QtWidgets.QApplication):
    def __init__(self, argv):
        super().__init__(argv)
        self.window = QtWidgets.QStackedWidget()
        self.window.setWindowTitle("Cookery App")
        self.ui = LoginForm()
        qss="css/style.qss"
        with open(qss,"r") as fh:
            style = fh.read()
            self.setStyleSheet(style)
            
        self.ui.setupUi(self.window)
        self.window.addWidget(self.ui)
        
        self.create_account = CreateAccountForm(parent=self.window)

        self.window.addWidget(self.create_account)
        
        self.window.show()


    
        