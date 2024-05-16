from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QFrame, QHBoxLayout, QVBoxLayout,QStackedWidget, QStackedLayout
from components import SideNav
from .dashboard import Dashboard
from .item_management import ItemManagement
from .add_item import AddItemPage
class AdminHomePage(QtWidgets.QFrame):

  def __init__(self, parent=None, user=None):
    super().__init__()
    self.parent = parent
    self.user = user
    self.setupUi()

  def setupUi(self):
    
    self.my_layout = QHBoxLayout(self)
    self.side_nav = SideNav(dashboard_clicked=self.on_dashboard_clicked, item_management_clicked=self.on_item_management_clicked, borrow_request_clicked=self.on_borrow_request_clicked, user_management_clicked=self.on_user_management_clicked, logout_clicked=self.on_logout_clicked)

    self.my_layout.addWidget(self.side_nav)
    self.main_frame = QFrame()
    self.main_frame.setObjectName("AdminHomePage")
    
    self.stacked_layout = QStackedLayout(self.main_frame)
    
    
    self.dashboard = Dashboard(self.stacked_layout)
    

    self.stacked_layout.addWidget(self.dashboard);
    self.stacked_layout.setCurrentWidget(self.dashboard)
    self.item_management = ItemManagement(self.stacked_layout)
    self.stacked_layout.addWidget(self.item_management)


    self.my_layout.addWidget(self.main_frame,1)

  def on_dashboard_clicked(self):
    self.stacked_layout.setCurrentWidget(self.dashboard)
  def on_item_management_clicked(self):
    self.stacked_layout.setCurrentWidget(self.item_management)
  def on_borrow_request_clicked(self):
    print("borrow request clicked")
  def on_user_management_clicked(self):
    print("user management clicked")
  def on_logout_clicked(self):
    self.parent.setCurrentIndex(0)


  
  