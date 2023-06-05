from flask import Blueprint, request

from ..data import ReadCsv, ReadJson, ReadXML
# import logging
# Need application log config
# logger = logging.getLogger('api')

api = Blueprint('api',__name__)


@api.route('/users', methods=['GET'])
def users():
    res = ReadJson.ReadJson().data
    return res, 200


@api.route('/user/<user_id>', methods=['GET', 'POST'])
def get_user_by_id(user_id):
    if request.method == 'GET':
        user_data = ReadJson.ReadJson().data
        
        if user_id not in user_data.keys():
            return "User not found", 400
        data = user_data[user_id]
        
        return data, 200
    
    elif request.method == 'POST':
        # verify payload data form data foramt payload
        payload_data = request.form
        keys = ['id', 'first_name', 'last_name', 'email']
        
        # check amy key is missing
        if  any([key not in payload_data.keys() for key in keys]):
            return "In-complete user data", 400
        
        # check empty string
        if any([value.strip() == "" for _, value in payload_data.items()]):
            return "Empty User Information", 400
        
        # check duplicate user_id
        new_id = payload_data['id']
        read_json = ReadJson.ReadJson()
        all_users = read_json.data
        
        # I assume new ID is from API input
        # If not generate one and drop new id duplicate check
        if new_id in all_users.keys():
            return "Invalid User ID", 400
        
        all_users['id'] = payload_data.to_dict()
        
        res = "New user has been created" 
        
        return res, 200
    
    
@api.route('/user/<user_id>/orders', methods=['GET'])
def get_user_order(user_id):
    user_orders = ReadXML.ReadXML().get_order_by_userid(user_id)
    return user_orders, 200


@api.route('/user/<user_id>/order_items', methods=['GET'])
def get_user_order_items(user_id):
    item_ids = ReadXML.ReadXML("orders.xml").get_items_by_userid(user_id)
    items_name = ReadCsv.ReadCsv("items.csv").get_items_by_id(item_ids)
    
    return items_name, 200