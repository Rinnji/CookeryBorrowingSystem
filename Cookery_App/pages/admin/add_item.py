from PyQt5.QtWidgets import QFrame, QGridLayout, QScrollArea, QVBoxLayout, QLabel, QHBoxLayout, QPushButton, QLineEdit, QFileDialog, QMessageBox
from models import Item
from . import item_management
from PyQt5 import QtCore
class AddItemPage(QFrame):

  def __init__(self, category,item_management_frame, parent):
    super().__init__()  
    self.parent = parent
    self.category = category
    self.setup_ui()
    self.item_management = item_management_frame 
  def setup_ui(self):
    self.setObjectName("add_item_page")
    self.vertical_layout = QHBoxLayout(self)

    self.grid_frame = QFrame()
    
    self.grid_frame.setObjectName("add_item_grid_frame")
    self.grid_frame.setFixedSize(800,700)
    self.grid_layout = QGridLayout(self.grid_frame)
    
    self.title = QLabel(f"Add {self.category.title()}")
    self.title.setObjectName("add_item_title")
    self.title.setStyleSheet("font-size: 50px;")
    self.title.setAlignment(QtCore.Qt.AlignCenter)
    self.grid_layout.addWidget(self.title,0,0, 1,2)
    
    

    self.name_label = QLabel("Name")
    self.grid_layout.addWidget(self.name_label,1,0, 1,1)
    self.name_input = QLineEdit()
    self.grid_layout.addWidget(self.name_input,1,1, 1,1)

    self.quantity_label = QLabel("Quantity")
    self.grid_layout.addWidget(self.quantity_label,2,0, 1,1)
    self.quantity_input = QLineEdit()
    self.grid_layout.addWidget(self.quantity_input,2,1, 1,1)


    

    self.image_label = QLabel("Image")
    self.grid_layout.addWidget(self.image_label,4,0, 1,1)
    self.image_input = QLineEdit()
    
    self.image_input.setReadOnly(True)
    self.image_input.mousePressEvent = self.open_file_dialog
    self.grid_layout.addWidget(self.image_input,4,1, 1,1,)


    self.add_button = QPushButton("Add")
    self.grid_layout.addWidget(self.add_button,5,1, 1,1, alignment=QtCore.Qt.AlignRight)
    self.add_button.setObjectName("item_add_button")
    self.add_button.clicked.connect(self.add_item)

    
      
    self.grid_layout.setAlignment(QtCore.Qt.AlignTop)
    self.grid_layout.setSpacing(20)
    self.vertical_layout.stretch(1)
    self.vertical_layout.addWidget(self.grid_frame,2,alignment=QtCore.Qt.AlignCenter)


  def open_file_dialog(self,event):
    file_dialog = QFileDialog()
    file_dialog.setFileMode(QFileDialog.ExistingFile)
    if file_dialog.exec_():
      file_path = file_dialog.selectedFiles()[0]
      self.image_input.setText(file_path)


  def add_item(self):
    name = self.name_input.text()
    quantity = self.quantity_input.text()
    
    image = self.image_input.text()
    if(name == '' or quantity == '' or image == ''):
      error_message = QMessageBox()
      error_message.setIcon(QMessageBox.Critical)
      error_message.setText("Please fill out all fields")
      error_message.setWindowTitle("Error")
      error_message.exec()
      return
    saved_image = Item.save_image(image)

   
    Item.save_item(Item(name=name.title(), quantity=quantity, image=saved_image, category=self.category))
    #add item to database
    #redirect to item management page
    
    new_item_management = item_management.ItemManagement(self.parent)
    self.parent.replaceWidget(self.item_management, new_item_management)
    self.parent.setCurrentWidget(new_item_management)