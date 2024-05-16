from PyQt5.QtWidgets import QFrame, QHBoxLayout, QLabel


class DashboardButton(QFrame):

  def __init__(self,text, on_click=None, image=""):
    super().__init__()
    self.text = text;
    self.orig_id = f"{self.text.lower()}_button"
    self.setup_ui()

  def setup_ui(self):
    self.setObjectName(self.orig_id)
    
    self.h_layout = QHBoxLayout(self)
    

    self.image_frame = QFrame()
    self.image_frame.setFixedSize(50,50)
    self.label = QLabel(self.text.title())
    self.setObjectName(self.orig_id)
    self.label.setStyleSheet("color:white;font-size: 20px;font-weight: bold;")
    self.h_layout.addStretch()
    self.h_layout.addWidget(self.image_frame)
    self.h_layout.addWidget(self.label)

  
    
