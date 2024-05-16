
from PyQt5 import QtCore, QtGui, QtWidgets

class CategoryPanel(QtWidgets.QFrame):
  def __init__(self, parent=None, name="", on_click = None):
    super().__init__()
    self.parent = parent
    self.name = name
    self.setupUi()
    self.on_click = on_click


  def setupUi(self):
    self.setFixedSize(400, 500)
    self.setObjectName("CategoryPanel")
    
    self.verticalLayout = QtWidgets.QVBoxLayout(self)
    self.label = QtWidgets.QLabel(self)
    self.label.setObjectName("title_label")
  
    self.label.setFont(QtGui.QFont('Arial', 40, QtGui.QFont.Bold))
    self.label.setAlignment(QtCore.Qt.AlignCenter)
    #when self is clicked
    self.label.mousePressEvent = self.clicked

    self.label.setText(self.name)
    self.verticalLayout.addWidget(self.label)

  def clicked(self, event):
    self.on_click(self.name)
    