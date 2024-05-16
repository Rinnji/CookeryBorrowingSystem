from PyQt5.QtWidgets import QFrame, QGridLayout, QScrollArea, QVBoxLayout, QLabel, QHBoxLayout, QPushButton
from models import Item
from pages.admin.add_item import AddItemPage

class ItemManagement(QFrame):
  def __init__(self, stacked_layout):
    super().__init__()
    self.refresh()
    self.stacked_layout = stacked_layout
    self.setup_ui()
    

  def setup_ui(self):
    
    self.setObjectName("item_management_page")

  
    self.grid_layout = QGridLayout(self)
    self.utensils_frame = self.add_list_frame("Utensils", self.utensils)
    self.grid_layout.addWidget(self.utensils_frame,0,0, 1,1)

    self.utensils_frame = self.add_list_frame("Plates", self.plates)
    self.grid_layout.addWidget(self.utensils_frame,1,0, 1,1)

    self.utensils_frame = self.add_list_frame("Glasses", self.glasses)
    self.grid_layout.addWidget(self.utensils_frame,0,1, 1,1)

    self.utensils_frame = self.add_list_frame("Others", self.others)
    self.grid_layout.addWidget(self.utensils_frame,1,1, 1,1)

  def add_list_frame(self, title, items):
    frame = QFrame()
    frame.setObjectName("list_frame")
    layout = QVBoxLayout(frame)

    h_frame = QFrame()
    h_layout = QHBoxLayout(h_frame)

    label = QLabel(title)
    label.setObjectName("title")
    h_layout.addWidget(label)

    add_button = QPushButton("+")
    add_button.setObjectName("add_button_list_frame")
    add_button.setMaximumWidth(50)

    add_button.clicked.connect(lambda: self.nav_to_add_item(title.lower()))
    h_layout.addWidget(add_button)


    layout.addWidget(h_frame,0)

    scroll_area = QScrollArea(self)
    scroll_area.setWidgetResizable(True)
    scroll_area.setObjectName("scroll_area_item_management")

    scroll_area_widget = QFrame()
    scroll_area_widget.setObjectName("scroll_widget")
    scroll_area_layout = QVBoxLayout(scroll_area_widget)
    label_frame = QFrame()
    label_frame.setObjectName("label_frame")
    label_layout = QHBoxLayout(label_frame)
    label_layout.addWidget(QLabel("Name"))
    label_layout.addWidget(QLabel("Quantity"))
    label_layout.addWidget(QLabel("Price"))
    scroll_area_layout.addWidget(label_frame)
    for obj in items:
      item_frame = QFrame()
      item_frame.setMaximumHeight(50)
      item_frame.setObjectName("item_frame")
      item_layout = QHBoxLayout(item_frame)
      item_layout.addWidget(QLabel(obj.name))
      item_layout.addWidget(QLabel(str(obj.quantity)))
      item_layout.addWidget(QLabel(str(obj.price)))
      scroll_area_layout.addWidget(item_frame)

    scroll_area_layout.addStretch(1)
    scroll_area.setWidget(scroll_area_widget)

    layout.addWidget(scroll_area,1)
    
    return frame
  

  def refresh(self):
    self.utensils = Item.get_items_by_item_type("utensils")
    self.plates = Item.get_items_by_item_type("plates")
    self.glasses = Item.get_items_by_item_type("glasses")
    self.others = Item.get_items_by_item_type("others")
    self.update()

  def nav_to_add_item(self, category):
    self.add_item_page = AddItemPage(category,self, self.stacked_layout)
    self.stacked_layout.addWidget(self.add_item_page)
    self.stacked_layout.setCurrentWidget(self.add_item_page)
    


   
  