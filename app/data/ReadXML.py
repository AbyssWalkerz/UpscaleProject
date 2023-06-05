import xmltodict
import os
from flask import current_app
class ReadXML:
 
    """Read XML File 
        For this project ORDER XML format
    """
    def __init__(self, file_name=None, path=None):
        if path is None:
            path = current_app.config['DATADIR']
        
        if file_name is None:
            file_name = current_app.config['ORDERS_XML'] 
               
        self.file_path = os.path.join(path, file_name)
        with open(self.file_path) as f:
            data =  xmltodict.parse(f.read())

        # Drive deep into XML information
        self.data = data['orders']['order']
    
    
    def get_order_by_userid(self, user_id):
        user_orders = [order_details for order_details in self.data
                       if order_details['user_id'] == user_id]
        
        return user_orders
    
    def get_items_by_userid(self, user_id):
        item_ids = [item['id'] for order in self.get_order_by_userid(user_id) for item in order['items']['item']]
        
        return item_ids