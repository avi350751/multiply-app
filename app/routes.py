from flask import Blueprint, request, jsonify

multiply_route = Blueprint('multiply_route', __name__)

@multiply_route.route('/multiply', methods=['POST'])
def multiply():
    data = request.get_json()
    num1 = data.get('num1')
    num2 = data.get('num2')
    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        return jsonify({'error': 'Invalid input, numbers required'}), 400
    
    result = num1 * num2
    return jsonify({'result': result}), 200