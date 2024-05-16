from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFrame, QVBoxLayout, QScrollArea, QHBoxLayout, QPushButton
from models import Item, Cart, Request
from components import CartItem

class CartList(QFrame):
  def __init__(self, parent, user):
    super().__init__()
    self.parent = parent
    self.user = user 
    self.setup_ui()

  def setup_ui(self):
    self.setObjectName("CartList")
    self.cart_list_layout = QVBoxLayout(self)
    self.scroll_frame = QScrollArea()
    self.scroll_frame.setObjectName("cart_list_scroll_frame")
    self.scroll_frame_layout = QVBoxLayout(self.scroll_frame)
    self.scroll_frame_layout.setObjectName("cart_list_scroll_frame_layout")
    self.scroll_frame.setWidgetResizable(True)
    

    self.scroll_content_frame = QFrame()
    self.scroll_content_frame.setObjectName("cart_list_scroll_content_frame")
    
    self.scroll_content_layout = QVBoxLayout(self.scroll_content_frame)
    self.scroll_content_layout.setObjectName("cart_list_scroll_content_layout")
   
 
    self.add_request_button = QPushButton()
    self.add_request_button.setObjectName("add_request_button")
    self.add_request_button.setText("Add Request")
    self.add_request_button.setFixedSize(200, 50)
    self.add_request_button.setStyleSheet("")
    self.add_request_button.clicked.connect(self.add_request_button_clicked)

    self.cart_list_layout.addWidget(self.add_request_button)
    cart_items = self.get_cart_items(self.user)
    
    for item in cart_items:
      item_panel = CartItem(item, self.user)
      self.scroll_content_layout.addWidget(item_panel)
      

    self.scroll_content_layout.addStretch()
    self.scroll_frame.setWidget(self.scroll_content_frame)
    self.cart_list_layout.addWidget(self.scroll_frame)
    

  def get_cart_items(self, user):
    #cart = Cart(user_id=user.id)
    self.cart = Cart.get_cart_by_user_id(user.id)
    cart_items = self.cart.items
    return cart_items
  
  def add_request_button_clicked(self):
    
    request = Request(user_id = self.user.id, items= self.cart.items)
    request.add_request()

  
    