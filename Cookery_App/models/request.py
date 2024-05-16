from .database import DatabaseModel
from .user_model import User
from .item import Item
class Request():

  def __init__(self, **kwargs):
    self.user_id = kwargs.get('user_id', None)
    self.quantity = kwargs.get('quantity', 0)
    self.items = kwargs.get('items', [])
    self.id = kwargs.get('id', None)
    self.user = kwargs.get('user', None)


  
  

  def add_request(self):
    
    def add_request(user_id):
      db=DatabaseModel().connect_db()
      cursor=db.cursor()
      sql = "INSERT INTO requests (user_id) VALUES (%s)"
      val = (user_id,)
      cursor.execute(sql, val)
      db.commit()
      db.close()
      return cursor.lastrowid
    
    
    self.id = add_request(self.user_id)
    db = DatabaseModel().connect_db()
    cursor = db.cursor()
    sql = "INSERT INTO request_items (request_id, item_id, quantity) VALUES (%s, %s, %s)"
    values = []
    for item in self.items:
      val = (self.id, item.id, item.quantity)
      values.append(val)
    cursor.executemany(sql, values)
      
    db.commit()
    db.close()

  @staticmethod
  def get_requests():
    db = DatabaseModel().connect_db()
    cursor = db.cursor(dictionary=True)
    sql = "SELECT requests.*, users.first_name,users.middle_name, users.last_name FROM requests JOIN users ON user_id = users.id"
    cursor.execute(sql)
    results = cursor.fetchall()
    
    requests = []
    for request in results:
      user = User(id = request['user_id'], first_name = request['first_name'],middle_name=request['middle_name'] ,last_name = request['last_name'])
      new_request = Request(id = request['id'], user_id = request['user_id'], user = user)
    
      requests.append(new_request)
    
    db.close()
    return requests


  @staticmethod
  def get_latest_requests():
    db = DatabaseModel().connect_db()
    cursor = db.cursor(dictionary=True)
    sql = "SELECT requests.*, users.first_name,users.middle_name, users.last_name FROM requests JOIN users ON user_id = users.id WHERE status = 'PENDING' ORDER BY id DESC LIMIT 10"
    cursor.execute(sql)
    results = cursor.fetchall()
    
    requests = []
    for request in results:
      user = User(id = request['user_id'], first_name = request['first_name'],middle_name=request['middle_name'] ,last_name = request['last_name'])
      new_request = Request(id = request['id'], user_id = request['user_id'], user = user)
    
      requests.append(new_request)
    
    db.close()
    return requests
  

  def get_items_from_request_id(request_id) -> Item: 
    db = DatabaseModel().connect_db()
    cursor = db.cursor(dictionary=True)
    sql = "SELECT request_items.*, items.name, items.image, items.quantity as item_quantity FROM request_items JOIN items ON item_id = items.id WHERE request_id = %s"

    val = (request_id,)
    cursor.execute(sql, val)
    results = cursor.fetchall()
    items = []
    for result in results:
      item = Item(id = result['item_id'], name = result['name'], quantity = result['item_quantity'], image = result['image'])
      item.quantity = result['quantity']
      items.append(item)

    db.close()
    return items
  

  @staticmethod 
  def approve_request(request_id):
    db = DatabaseModel().connect_db()
    cursor = db.cursor()
    sql = "UPDATE requests SET status = 'APPROVED' WHERE id = %s"
    val = (request_id,)
    cursor.execute(sql, val)
    db.commit()
    db.close()

  @staticmethod
  def reject_request(request_id):
    db = DatabaseModel().connect_db()
    cursor = db.cursor()
    sql = "UPDATE requests SET status = 'REJECTED' WHERE id = %s"
    val = (request_id,)
    cursor.execute(sql, val)
    db.commit()
    db.close()