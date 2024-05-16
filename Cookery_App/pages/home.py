
from PyQt5 import QtCore, QtGui, QtWidgets
from models import User
from components import CategoryPanel
from .items_list import ItemsList
from .cart import CartList

class HomePage(QtWidgets.QFrame):


  def __init__(self, parent=None,user=None):
    super().__init__()
    self.parent = parent;
    self.user = user
    self.setupUi()

  def setupUi(self):

    self.categories = ['utensils', 'glasses', 'plates','others']
    
    self.setObjectName("HomePage")
  
    
    #Home Page
    self.mainPanel = QtWidgets.QVBoxLayout(self)
    self.mainPanel.setObjectName("mainPanel")
    self.mainPanel.setContentsMargins(0, 0, 0, 0)
    self.mainPanel.setSpacing(0)
    self.add_navbar()
    self.stacked_frame = QtWidgets.QStackedWidget(self)

    #category page
    self.add_category_frame()

    #cart page
    
    
    
    self.stacked_frame.addWidget(self.category_frame)
    self.mainPanel.addWidget(self.stacked_frame)
  def scrollAreaWheelEvent(self, event):
    
    self.scrollArea.horizontalScrollBar().setValue(self.scrollArea.horizontalScrollBar().value() - event.angleDelta().y())
    event.accept()

  def add_navbar(self):
    self.header = QtWidgets.QFrame(self)
    self.header.setObjectName("navbar")
    self.header.setMinimumSize(QtCore.QSize(0, 60))
    self.header.setMaximumSize(QtCore.QSize(16777215, 60))



    self.horizontalLayout = QtWidgets.QHBoxLayout(self.header)
    #self.horizontalLayout.setObjectName("")
    self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
    self.horizontalLayout.setSpacing(0)
    self.horizontalLayout.setStretch(0, 0)

    self.header_label = QtWidgets.QLabel(self.header)
    self.header_label.setObjectName("nav-logo")
    self.header_label.setText("Cookery")
    self.header_label.setMaximumWidth(500)
    self.horizontalLayout.addWidget(self.header_label)
    
    self.button_frame = QtWidgets.QFrame(self.header)
    self.button_frame.setObjectName("button_frame")
    self.horizontalLayout.addWidget(self.button_frame, 0, QtCore.Qt.AlignLeft)
    self.button_frame_layout = QtWidgets.QHBoxLayout(self.button_frame)
    
    self.home_button = QtWidgets.QPushButton(self.header)
    self.home_button.setObjectName("home_button")
    self.home_button.setText("Home")
    self.home_button.setMinimumWidth(200)
    self.home_button.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
    self.home_button.clicked.connect(self.home_button_clicked)
    
    self.borrowed_items_button = QtWidgets.QPushButton(self.header)
    self.borrowed_items_button.setObjectName("borrowed_items_button")
    self.borrowed_items_button.setText("Borrowed Items")
    self.borrowed_items_button.setMinimumWidth(200)
    self.borrowed_items_button.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
    
    self.cart_button = QtWidgets.QPushButton(self.header)
    self.cart_button.setObjectName("cart_button")
    self.cart_button.setText("Cart")
    self.cart_button.setMinimumWidth(200)
    self.cart_button.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
    self.cart_button.clicked.connect(self.cart_button_clicked)


    self.logout_button = QtWidgets.QPushButton(self.header)
    self.logout_button.setObjectName("logout_button")
    self.logout_button.setText("Logout")
    self.logout_button.setMinimumWidth(200)
    self.logout_button.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
    self.logout_button.clicked.connect(self.logout)

    self.button_frame_layout.addWidget(self.home_button, 0, QtCore.Qt.AlignLeft)
    self.button_frame_layout.addWidget(self.borrowed_items_button, 0, QtCore.Qt.AlignLeft)
    self.button_frame_layout.addWidget(self.cart_button, 0, QtCore.Qt.AlignLeft)
    self.button_frame_layout.addWidget(self.logout_button, 0, QtCore.Qt.AlignRight)


    self.mainPanel.addWidget(self.header)
  
  def add_category_frame(self):

    self.category_frame = QtWidgets.QFrame(self.stacked_frame)
    self.category_frame.setObjectName("category_frame")
    self.category_frame_layout = QtWidgets.QVBoxLayout(self.category_frame)
    self.category_frame_layout.setObjectName("category_frame_layout")
   
    self.scrollArea = QtWidgets.QScrollArea(self.category_frame)
    self.scrollArea.setWidgetResizable(True)
   
    self.scrollArea.setObjectName("UtensilsScrollArea")
    #self.scrollArea.setStyleSheet("background:blue;")
    self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
    self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
    self.scrollAreaWidgetContents = QtWidgets.QFrame()
    self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

    self.scrollAreaWidgetLayout = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents)
    #mousewheel on scrollArea
    self.scrollAreaWidgetLayout.setObjectName("scrollAreaWidgetLayout")
    self.scrollArea.wheelEvent = self.scrollAreaWheelEvent

    self.scrollArea.setWidget(self.scrollAreaWidgetContents)

    for category in self.categories:
      self.category_panel = CategoryPanel(self.scrollAreaWidgetContents, name=category, on_click=self.category_panel_clicked)
      self.scrollAreaWidgetLayout.addWidget(self.category_panel)

    self.category_frame_layout.addWidget(self.scrollArea)



  def category_panel_clicked(self, item_type):
    item_list = ItemsList(self,item_type)
    self.stacked_frame.addWidget(item_list)
    self.stacked_frame.setCurrentWidget(item_list)

  def home_button_clicked(self):
    #self.add_category_frame()
    self.stacked_frame.setCurrentWidget(self.category_frame)

  def cart_button_clicked(self):
    
    self.cart_frame = CartList(self, self.user)
    self.stacked_frame.addWidget(self.cart_frame)
    self.stacked_frame.setCurrentWidget(self.cart_frame)


  def logout(self):
    self.parent.setCurrentIndex(0)
    #for widget in self.parent.children()[3:]:
     # self.parent.removeWidget(widget)


  def remove_widgets(self):
    for child in self.stacked_frame.children():
      self.stacked_frame.removeWidget(child)