from .database import DatabaseModel
from .item import Item

class Cart():

  def __init__(self, **kwargs):
    self.user_id = kwargs.get('user_id', None)
    self.quantity = kwargs.get('quantity', 0)
    self.items = kwargs.get('items', [])
    self.id = kwargs.get('id', None)
    

  def add_cart(self):
    db = DatabaseModel().connect_db()
    cursor = db.cursor()
    sql = "INSERT INTO cart (user_id, item_id, quantity) VALUES (%s, %s, %s) ON DUPLICATE KEY UPDATE quantity = quantity + VALUES(quantity)"
    values = []
    for item in self.items:
      val = (self.user_id, item.id, item.quantity)
      values.append(val)
    cursor.executemany(sql, values)
      
    db.commit()
    db.close()


  def add(self,item):
    self.items.append(item)

  @staticmethod
  def get_cart_by_user_id(user_id):
    db = DatabaseModel().connect_db()
    cursor = db.cursor(dictionary=True)
    sql = "SELECT cart.*, items.name,items.image, items.quantity as item_quantity FROM cart JOIN items ON item_id = items.id WHERE user_id = %s"
    val = (user_id,)
    cursor.execute(sql, val)
    results = cursor.fetchall()
    
    items = []
    for cart in results:
      item = Item(id = cart['item_id'], name = cart['name'], quantity = cart['quantity'], image = cart['image'])
      items.append(item)
    
    cart = Cart(user_id = user_id, items = items)
    db.close()
    return cart

  @staticmethod
  def decrement_quantity(user_id, item_id):
    db = DatabaseModel().connect_db()
    cursor = db.cursor()
    sql = "UPDATE cart SET quantity = quantity - 1 WHERE user_id = %s AND item_id = %s"
    val = (user_id, item_id)
    cursor.execute(sql, val)
    db.commit()
    db.close()


  @staticmethod
  def increment_quantity(user_id, item_id):
    
    db = DatabaseModel().connect_db()
    cursor = db.cursor()
    sql = "UPDATE cart SET quantity = quantity + 1 WHERE user_id = %s AND item_id = %s"
    val = (user_id, item_id)
    cursor.execute(sql, val)
    db.commit()
    db.close()
  

  def clear(self):
    db = DatabaseModel().connect_db()
    cursor = db.cursor()
    sql = "DELETE FROM cart WHERE user_id = %s"
    val = (self.user_id,)
    cursor.execute(sql, val)
    db.commit()
    db.close()