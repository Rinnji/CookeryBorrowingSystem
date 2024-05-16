from PyQt5.QtWidgets import QFrame, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QLineEdit, QDialogButtonBox, QMessageBox
from models import Cart
class CartItem(QFrame):

  def __init__(self, item,user):
    super().__init__()
    self.user = user
    self.item = item
   
    self.setup_ui()

  def setup_ui(self):
    self.setObjectName("CartItem")
    self.setMaximumHeight(200)
    self.cart_item_layout = QHBoxLayout(self)

    self.image = QFrame(self)
    self.image.setObjectName("cart_item_image")
    self.image.setStyleSheet(f"border-image: url(images/{self.item.image})  0 0 0 0 center center;border-radius: 10px")
    self.image.setFixedSize(180, 180)
    

    self.details_frame = QFrame(self)
    self.details_frame.setObjectName("cart_item_details_frame")
    self.details_layout = QVBoxLayout(self.details_frame)
    self.details_layout.setObjectName("cart_item_details_layout")
    #make label
    self.title_label = QLabel(self.item.name.title())
    self.title_label.setObjectName("cart_item_title")

    self.quantity_label = QLabel(f"Quantity: {self.item.quantity}")
    self.quantity_label.setObjectName("cart_item_quantity")
    #add label
    self.details_layout.addWidget(self.title_label)

    self.quantity_frame = self.add_quantiy_frame()
    self.details_layout.addWidget(self.quantity_frame)
    self.details_layout.addStretch()
    #add to self
    self.cart_item_layout.addWidget(self.image)
    self.cart_item_layout.addWidget(self.details_frame)


  def add_quantiy_frame(self):
    quantity_frame = QFrame(self)
    quantity_frame.setObjectName("quantity_frame")
    quantity_frame_layout = QHBoxLayout(quantity_frame)
    quantity_frame.setObjectName("quantity_frame_layout")
    quantity_frame.setFixedSize(150, 50)

    self.decrement_button = QPushButton(self)
    self.decrement_button.setObjectName("decrement_button")
    self.decrement_button.setText("-")
    self.decrement_button.setFixedSize(25, 25)
    self.decrement_button.clicked.connect(self.decrement_quantity)

    self.quantity_input = QLineEdit(self)
    self.quantity_input.setObjectName("quantity_input")
    self.quantity_input.setText(str(self.item.quantity))
    self.quantity_input.setReadOnly(True)
    self.quantity_input.setFixedSize(25, 25)

    self.increment_button = QPushButton(self)
    self.increment_button.setObjectName("increment_button")
    self.increment_button.setText("+")
    self.increment_button.setFixedSize(25, 25)
    self.increment_button.clicked.connect(self.increment_quantity)

    quantity_frame_layout.addWidget(self.decrement_button)
    quantity_frame_layout.addWidget(self.quantity_input)
    quantity_frame_layout.addWidget(self.increment_button)

    self.cart_item_layout.addWidget(quantity_frame)

    return quantity_frame
  
  def decrement_quantity(self):
    current_quantity = int(self.quantity_input.text())
    if current_quantity > 1:
      Cart.decrement_quantity( self.user.id,self.item.id)
      self.quantity_input.setText(str(current_quantity - 1))
      self.item.quantity = current_quantity - 1
    else:
      message_box = QMessageBox()
      message_box.setObjectName("dialog_box")
      dialog = message_box.question(self,"Cookery", "Are you sure you want to remove the item from the cart?", QMessageBox.Yes| QMessageBox.No)
      print(dialog, QMessageBox.Yes)
      

  def increment_quantity(self):
    current_quantity = int(self.quantity_input.text())
    Cart.increment_quantity( self.user.id,self.item.id)
    self.quantity_input.setText(str(current_quantity + 1))
    self.item.quantity = current_quantity + 1

  def remove_item(self):
    print("removing item from cart...")


  def get_item(self):
    return self.item

  
    