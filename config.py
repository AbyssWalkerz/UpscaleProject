import os

class Config:
    # any application config 
    
    SECRET_KEY = 'ABCD'
    # Appliation database config
    BASEDIR =  os.path.abspath(os.path.dirname(__file__))
    DATABASE_FILE = os.path.join(BASEDIR, "database", "database.db")
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{DATABASE_FILE}'
    
    # Project's data source
    DATADIR =  os.path.join(BASEDIR, "app", "database") 
    ORDERS_XML = 'orders.xml'
    ITEMS_CSV = 'items.csv'
    USERS_JSON = 'users.json'