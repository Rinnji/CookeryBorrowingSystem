from .database import DatabaseModel

class User():

  USER = 'user'
  ADMIN = 'admin'

  def __init__(self, **kwargs):
    self.name = kwargs.get('name', '')
    self.email = kwargs.get('email', '')
    self.password = kwargs.get('password', '')
    self.id = kwargs.get('id', None)
    self.created_at = kwargs.get('created_at', None)
    self.first_name = kwargs.get('first_name', '')
    self.last_name = kwargs.get('last_name', '')
    self.middle_name = kwargs.get('middle_name', '')
    self.user_type = kwargs.get('user_type', self.USER)
    self.username = kwargs.get('username', '')


  
  def save(self):
    db = DatabaseModel().connect_db()
    cursor = db.cursor()
    self.process_name()
    self.password = DatabaseModel().hash_string(self.password)
    sql = "INSERT INTO users (email, password, first_name, last_name, middle_name, user_type) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (self.email, self.password, self.first_name, self.last_name, self.middle_name, self.user_type)
    cursor.execute(sql, val)
    db.commit()
    self.id = cursor.lastrowid
    db.close()

  
  @staticmethod
  def login(email, password):
    db = DatabaseModel().connect_db()
    cursor = db.cursor(dictionary=True)
    password = DatabaseModel().hash_string(password)
    sql = "SELECT * FROM users WHERE email = %s AND password = %s"
    val = (email, password)
    cursor.execute(sql, val)
    user = cursor.fetchone()
    db.close()
    if(user):
      return User(**user)
    else: 
      return None
  
  def process_name(self):
    nameArr = self.name.split(' ')
    
    if(len(nameArr) > 2):
      *first_name, self.middle_name, self.last_name = nameArr
      self.first_name = ' '.join(first_name)
      
    else:
      self.first_name = nameArr[0]
      self.middle_name = ''
      self.last_name = nameArr[-1]
  




