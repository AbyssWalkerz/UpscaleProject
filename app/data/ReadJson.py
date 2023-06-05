import json
import os
from flask import current_app

class ReadJson:
    def __init__(self, flie_name=None, path=None):
        
        if path is None:
            path = current_app.config['DATADIR']
        
        if file_name is None:
            file_name = current_app.config['USERS_JSON']             
        
        self.file_path = os.path.join(path, flie_name)
        with open(self.file_path) as f:
            self.data = json.load(f)
    
    def get_data_by_key(self, key):
        return self.data.get(key)
    
    def write_back(self, data):
        with open(self.file_path, "w") as outfile:
            json.dump(data, outfile)
    
 