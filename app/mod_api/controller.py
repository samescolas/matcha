from flask import Blueprint, jsonify, request
from .. import User

api = Blueprint('api', __name__, template_folder="static/templates", static_folder="static")

def jsonify_user_record(record):
	return {
		'user_id': record[0],
		'f_name': record[1],
		'l_name': record[2],
		'age': record[4],
		'gender': record[5],
		'location_id': record[7],
		'sexual_preference': record[10],
		'active': record[11]
	}

@api.route('/users', methods=['GET'])
def get_all_users():
	user = User('')
	if not user.db.get('users', '1', '1'):
		return jsonify({'message': 'No users found.'}), 403
	users = user.db.results[:]
	obj = {}
	for record in users:
		obj[record[0]] = jsonify_user_record(record)
	del user
	return jsonify({'data': obj})

@api.route('/users', methods=['POST'])
def create_user():
	print('inside create_user')
	data = request.get_json()
	print('here')
	if 'email' not in data or 'passwd' not in data:
		return jsonify({'message': 'Something went wrong.'}), 403
	print('also here')
	user = User(data['email'])
	if not user.available:
		return jsonify({'message': 'Email already registered.'}), 403
	id = user.add()
	if id == None:
		return jsonify({'message': 'Something went wrong.'}), 403
	else:
		return jsonify({'message': 'Success', 'user_id': id}), 200

@api.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
	user = User('')
	if not user.db.get('users', 'id', user_id):
		return jsonify({'message': 'No users found.'}), 403
	obj = jsonify_user_record(user.db.results[0])
	del user
	return jsonify({'data': obj}), 200

# this will be used to update user info
@api.route('/users/<user_id>', methods=['PUT'])
def update_user_info(user_id):
	return '', 200

@api.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
	return '', 200
