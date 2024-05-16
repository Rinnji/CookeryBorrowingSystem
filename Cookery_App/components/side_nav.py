from PyQt5.QtWidgets import QFrame, QVBoxLayout, QPushButton
from PyQt5.QtGui import QMouseEvent
from .dashboard_button import DashboardButton

class SideNav(QFrame):

  def __init__(self, dashboard_clicked=None, item_management_clicked=None, borrow_request_clicked=None, user_management_clicked=None, logout_clicked=None):
    super().__init__()
    self.buttons = {}
    self.dashboard_clicked = dashboard_clicked
    self.item_management_clicked = item_management_clicked
    self.borrow_request_clicked = borrow_request_clicked
    self.user_management_clicked = user_management_clicked
    self.logout_clicked = logout_clicked
    self.setup_ui()



  def setup_ui(self):
    self.setObjectName("side_nav")
    self.setFixedWidth(300)
    
    self.nav_layout = QVBoxLayout(self)
    self.add_buttons()
    

  def add_buttons(self):
    self.dashboard_button = DashboardButton("Dashboard")
    self.dashboard_button.setObjectName("side_nav_active")
    self.item_management_button = DashboardButton("Item Management")
    self.borrow_requests_button = DashboardButton("Borrow Request")
    self.user_management_button = DashboardButton("User Management")

    self.logout_button = DashboardButton("Logout")
    
    self.nav_layout.addWidget(self.dashboard_button)
    self.nav_layout.addWidget(self.item_management_button)
    self.nav_layout.addWidget(self.borrow_requests_button)
    self.nav_layout.addWidget(self.user_management_button)  
    self.nav_layout.addStretch()
    self.nav_layout.addWidget(self.logout_button)

    self.buttons['dashboard_button'] = (self.dashboard_button, self.dashboard_clicked)
    self.buttons['item_management_button'] = (self.item_management_button, self.item_management_clicked)  
    self.buttons['borrow_requests_button'] = (self.borrow_requests_button, self.borrow_request_clicked)
    self.buttons['user_management_button'] = (self.user_management_button, self.user_management_clicked)
    self.buttons['logout_button'] = (self.logout_button, self.logout_clicked)
    
    self.dashboard_button.mousePressEvent = lambda event: self.on_button_clicked(self.dashboard_button)

    self.item_management_button.mousePressEvent = lambda event: self.on_button_clicked(self.item_management_button)

    self.borrow_requests_button.mousePressEvent = lambda event: self.on_button_clicked(self.borrow_requests_button)

    self.user_management_button.mousePressEvent = lambda event: self.on_button_clicked(self.user_management_button)

    self.logout_button.mousePressEvent = lambda event: self.on_button_clicked(self.logout_button)

  def on_button_clicked(self,  button):
    
    for b, func in self.buttons.values():
      if button != b:
        b.setObjectName(b.orig_id)
        b.setStyleSheet(f"#{b.objectName()}" +"{background: rgba(0,0,0,0)}")
      else:
        b.setObjectName("side_nav_active") 
        b.setStyleSheet("""#side_nav_active {background:rgb(0,0,0);
          border-radius: 30px;
          border: 3px solid white;}""")
        func()
    
   