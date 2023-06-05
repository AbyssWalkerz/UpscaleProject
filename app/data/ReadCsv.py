from flask import current_app
import pandas as pd
import os

class ReadCsv:
    def __init__(self, file_name=None, path=None):
        """Read CSV to Pandas dataframe

        Args:
            file_name (str, optiona): csv file name
            path (str, optional): path to file. Defaults to None.
        """
        if path is None:
            path = current_app.config['DATADIR']
        
        if file_name is None:
            file_name = current_app.config['ITEMS_CSV'] 
        
        file_path = os.path.join(path, file_name)
        self.dataset = pd.read_csv(file_path, dtype=str)
    
    
    def get_items_by_id(self, ids):
        item_name = self.dataset[self.dataset['id'].isin(ids)]['name'].to_list()
        return item_name
    
    
    