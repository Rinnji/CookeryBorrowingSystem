from PyQt5.QtWidgets import QFrame, QGridLayout, QScrollArea, QVBoxLayout, QLabel, QHBoxLayout
from .view_request import RequestView
from models import Request
class Dashboard(QFrame):

  def __init__(self, parent):
    super().__init__()
    self.parent = parent
    self.setup_ui()
    

  def setup_ui(self):
    self.setObjectName("dashboard")
    self.dashboard_layout = QHBoxLayout(self)
    self.add_scroll_area()
    self.add_most_borrowed_items()

    #add_gap

    

  
  def add_scroll_area(self):
    requests = Request.get_latest_requests()
    self.latest_request_frame = QFrame()
    self.latest_request_frame.setObjectName("latest_request_frame")
    self.latest_request_layout = QVBoxLayout(self.latest_request_frame)
    self.latest_request_label = QLabel("Latest Requests")
    self.latest_request_label.setObjectName("title")
    self.latest_request_layout.addWidget(self.latest_request_label,0)

    
    self.scroll_area = QScrollArea(self)
    self.scroll_area.setWidgetResizable(True)
    self.scroll_area.setObjectName("latest_request_scroll_area")

    self.scroll_area_widget = QFrame()
    self.scroll_area_widget.setObjectName("latest_request_scroll_widget")
    self.scroll_area_layout = QVBoxLayout(self.scroll_area_widget)


    
    request_label_frame = QFrame()
    request_label_frame.setObjectName("request_label_frame")
    request_label_layout = QHBoxLayout(request_label_frame)
    request_id_label = QLabel("Request ID")
    request_user_label = QLabel("User")

    request_label_layout.addWidget(request_id_label)
    request_label_layout.addWidget(request_user_label)
    self.scroll_area_layout.addWidget(request_label_frame)
    for request in requests:
      request_panel = self.add_request(request)
      self.scroll_area_layout.addWidget(request_panel)

    self.scroll_area_layout.addStretch()
    self.scroll_area.setWidget(self.scroll_area_widget)
    
    self.latest_request_layout.addWidget(self.scroll_area,1)
    self.dashboard_layout.addWidget(self.latest_request_frame,1)
    

  def add_most_borrowed_items(self):
    self.borrowed_items_frame = QFrame()
    self.borrowed_items_frame.setObjectName("borrowed_items_frame")
    self.setMinimumWidth(500)
    self.borrowed_items_layout = QVBoxLayout(self.borrowed_items_frame)
    self.borrowed_items_label = QLabel("Most Borrowed Items")
    self.borrowed_items_layout.addWidget(self.borrowed_items_label)

    self.dashboard_layout.addWidget(self.borrowed_items_frame,1)

    

  def add_request(self,request):
    request_frame = QFrame()
    request_frame.setFixedHeight(60)
    request_frame.setObjectName("request_frame")
    request_layout = QHBoxLayout(request_frame)
    request_id_label = QLabel(str(request.id))

    request_user_label = QLabel(f"{request.user.first_name} {request.user.middle_name} {request.user.last_name}")
    
    request_layout.addWidget(request_id_label)
    request_layout.addWidget(request_user_label)
    
    request_frame.mousePressEvent = lambda event: self.view_request(request)
    return request_frame
  

  def view_request(self, request):
    view_request = RequestView(self.parent, request)
    self.parent.addWidget(view_request)
    self.parent.setCurrentWidget(view_request)
