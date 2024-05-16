

from PyQt5 import QtCore, QtGui, QtWidgets
from models import Item, Cart

class ItemsList(QtWidgets.QFrame):

  def __init__(self,parent, category):
    super().__init__()
    self.category = category
    self.items = Item.get_items_by_item_type(category)
    self.parent = parent
    self.setupUi()

  def setupUi(self):
   
    self.setObjectName("ItemsList")
    self.verticalLayout = QtWidgets.QVBoxLayout(self)
    self.verticalLayout.setObjectName("ItemListLayout")
    self.verticalLayout.setContentsMargins(0, 0, 0, 0)
    self.verticalLayout.setSpacing(0)

    self.title = QtWidgets.QLabel(self);
    self.title.setObjectName("title")
    self.title.setText(self.category.title())
    self.title.setAlignment(QtCore.Qt.AlignCenter)
    self.verticalLayout.addWidget(self.title)

   
    self.scrollbar_frame = QtWidgets.QScrollArea(self)
    self.scrollbar_frame.setObjectName("item_list_scrollbar_frame")
    self.scrollbar_frame_layout = QtWidgets.QVBoxLayout(self.scrollbar_frame)
    self.scrollbar_frame_layout.setObjectName("item_list_scrollbar_frame_layout")

    self.scrollArea = QtWidgets.QScrollArea(self.scrollbar_frame)
    self.scrollArea.setWidgetResizable(True)
    self.scrollArea.setObjectName("item_list_scrollArea")
    self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
    self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
    self.scrollAreaWidgetContents = QtWidgets.QFrame()
    self.scrollAreaWidgetContents.setObjectName("item_list_scrollAreaWidgetContents")
    self.scrollAreaWidgetLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
    self.scrollAreaWidgetLayout.setObjectName("item_list_scrollAreaWidgetLayout")
    self.scrollAreaWidgetLayout.columnCount = 1
    self.scrollArea.setWidget(self.scrollAreaWidgetContents)
    
    row = 0;
    column = 0;
    for item in self.items:
      if column == 3:
        row += 1
        column = 0
      print("hello")
      item_panel = self.add_item(item)
      self.scrollAreaWidgetLayout.addWidget(item_panel, row, column)
      column += 1
    self.scrollbar_frame_layout.addWidget(self.scrollArea)
    self.verticalLayout.addWidget(self.scrollbar_frame)
   
  def add_item(self, item):
    
    item_frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
    item_frame.setObjectName("item_frame_list")
    #
    item_frame_class = "#item_frame_list{%s}" % f'border-image: url("images/{item.image}") no-repeat center center'
  
    print(item_frame_class)
    item_frame.setFixedSize(300, 300)
    item_frame.setStyleSheet(item_frame_class)
    item_frame_layout = QtWidgets.QHBoxLayout(item_frame)
    item_frame_layout.setObjectName("item_frame_layout")
    item_frame_layout.setContentsMargins(0,0,0,0)
    item_frame.setContentsMargins(0,0,0,0)

    cover_frame = QtWidgets.QFrame(item_frame)
    cover_frame.setObjectName("cover_frame")
    cover_frame_layout = QtWidgets.QVBoxLayout(cover_frame)
    cover_frame_layout.setObjectName("cover_frame_layout")

    item_name = QtWidgets.QLabel(f"+\n{item.name.title()}")
    item_name.setObjectName("item_name")
    #item_name.setText(item.name)
    item_name.setAlignment(QtCore.Qt.AlignCenter)
    cover_frame_layout.addWidget(item_name)
    item_frame_layout.addWidget(cover_frame, 1)
    item_frame.mousePressEvent = lambda event : self.add_to_cart(item)
    
    #self.scrollAreaWidgetLayout.addWidget(item_frame)
    return item_frame

  def add_to_cart(self, item):
    item.quantity = 1
    Cart(user_id = self.parent.user.id, items = [item] ).add_cart()

    buttonBox = QtWidgets.QDialogButtonBox()
    layout = QtWidgets.QVBoxLayout()
    message = QtWidgets.QLabel(f"{item.name.title()} added to cart!")
    layout.addWidget(message)
    layout.addWidget(buttonBox)
    
    dialog = QtWidgets.QDialog(self)
    dialog.setObjectName("dialog_box")
    dialog.setLayout(layout)
    dialog.setWindowTitle("Cookery App")
    dialog.exec()
    