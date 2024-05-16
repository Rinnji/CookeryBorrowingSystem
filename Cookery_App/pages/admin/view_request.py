from PyQt5.QtWidgets import QFrame, QVBoxLayout, QScrollArea, QHBoxLayout, QPushButton, QLabel, QMessageBox
from models import Request
from . import dashboard
class RequestView(QFrame):
  
  def __init__(self,parent, request):
    super().__init__()
    self.parent = parent

    
    self.request = request
    request.items = Request.get_items_from_request_id(request.id)
    self.setup_ui()

  def setup_ui(self):
    print(self.request.items)
    self.setObjectName("RequestView")
    self.request_layout = QVBoxLayout(self)

    self.center_frame = QFrame()
    self.center_layout = QVBoxLayout(self.center_frame)
    self.center_frame.setObjectName("request_center_frame")

    self.title = QLabel("Request ID: " + str(self.request.id))
    self.title.setObjectName("title")

    self.user_label = QLabel("User: " + f"{self.request.user.first_name} {self.request.user.last_name}".title())
    self.user_label.setObjectName("title")

    self.scroll_area = QScrollArea()
    self.scrollAreaLayout = QVBoxLayout(self.scroll_area)
    self.scroll_area.setObjectName("request_scroll_area")
    
    self.scroll_area_widget = QFrame()
    self.scroll_area_layout = QVBoxLayout(self.scroll_area_widget)  


    request_label_frame = QFrame()
    request_label_frame.setObjectName("item_frame")
    request_label_layout = QHBoxLayout(request_label_frame)
    request_number_label = QLabel("#")
    request_id_label = QLabel("Item")
    request_user_label = QLabel("Quantity")
    
    request_label_layout.addWidget(request_number_label)
    request_label_layout.addWidget(request_id_label)
    request_label_layout.addWidget(request_user_label)

    self.scroll_area_layout.addWidget(request_label_frame)

    for index, item in enumerate(self.request.items,1):
      item_frame = self.add_item(item, index)
      self.scroll_area_layout.addWidget(item_frame)

  
    self.scrollAreaLayout.addWidget(self.scroll_area_widget)
    self.scroll_area_layout.addStretch()
    self.center_layout.addWidget(self.title)
    self.center_layout.addWidget(self.user_label)
    self.center_layout.addWidget(self.scroll_area)
    self.center_layout.addStretch()
    
    self.button_frame = QFrame()
    self.button_frame_layout = QHBoxLayout(self.button_frame)
    self.button_frame.setObjectName("button_frame")



    self.approve_button = QPushButton("Approve")
    self.approve_button.setObjectName("approve_button")
    self.approve_button.clicked.connect(lambda: self.approve_request())

    self.reject_button = QPushButton("Reject")
    self.reject_button.setObjectName("reject_button")
    self.reject_button.clicked.connect(lambda: self.reject_request())

    self.button_frame_layout.addStretch()
    self.button_frame_layout.addWidget(self.reject_button)
    self.button_frame_layout.addWidget(self.approve_button)

    self.center_layout.addWidget(self.button_frame)
    self.request_layout.addWidget(self.center_frame)


  def add_item(self,item, ind):
    item_frame = QFrame()
    item_frame.setObjectName("item_frame")
    
    item_layout = QHBoxLayout(item_frame)
    item_num_label = QLabel(str(ind))
    item_name_label = QLabel(item.name)
    item_quantity_label = QLabel(str(item.quantity))
    
    item_layout.addWidget(item_num_label)
    item_layout.addWidget(item_name_label)
    item_layout.addWidget(item_quantity_label)
    
    return item_frame
  
  def approve_request(self):
    Request.approve_request(self.request.id)
    QMessageBox.about(self, "Success", "Request Approved")
    new_dashboard = dashboard.Dashboard(self.parent)
    self.parent.replaceWidget(self.parent.itemAt(0).widget(), new_dashboard)
    self.parent.setCurrentIndex(0)
    


  def reject_request(self):
    Request.reject_request(self.request.id)
    QMessageBox.about(self, "Success", "Request Rejected")
    new_dashboard = dashboard.Dashboard(self.parent)
    self.parent.replaceWidget(self.parent.itemAt(0).widget(), new_dashboard)
    self.parent.setCurrentIndex(0)