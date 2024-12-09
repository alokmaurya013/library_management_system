import functools
from flask import request, jsonify
import jwt
import datetime
from .models import Member

SECRET_KEY = 'mysecretkey'

def token_required(f):
    @functools.wraps(f)
    def decorated_function(*args, **kwargs):
        auth_header = request.headers.get('Authorization')
        if not auth_header:
            return jsonify({'message': 'Token is missing!'}), 403

        parts = auth_header.split()
        if len(parts) != 2 or parts[0].lower() != 'bearer':
            return jsonify({'message': 'Token format is invalid!'}), 403

        token = parts[1]
        try:
            decoded_token = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            current_user = Member.query.get(decoded_token['user_id'])  
            if not current_user:
                return jsonify({'message': 'User not found!'}), 404
        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Token has expired!'}), 403
        except jwt.InvalidTokenError:
            return jsonify({'message': 'Invalid token!'}), 403

        return f(current_user, *args, **kwargs) 
    return decorated_function

def create_token(user_id):
    expiration = datetime.datetime.utcnow() + datetime.timedelta(hours=1) 
    payload = {
        'user_id': user_id,
        'exp': expiration
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    return token

