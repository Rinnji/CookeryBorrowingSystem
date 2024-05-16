import mysql.connector
import hashlib
class DatabaseModel:

  mydb = None
  def connect_db(self):
    self.mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    database="cookery_db"
    )
    
    return self.mydb



  def hash_string(self, s):
    s_bytes = s.encode('utf-8')
    hash_object = hashlib.sha256(s_bytes)
    return hash_object.hexdigest()