'''
Created on 23 Aug 2017

@author: havannavar
'''

from flask import jsonify, make_response, request
from functools import wraps
import re

def validate(f):      
    
    @wraps(f)
    def decorated(*args, **kwargs):
        email = request.json.get('email')
        if email is None:
            # Unauthorized
            return make_response(jsonify({'message':'Provide the email'}), 401)
        else:
            if len(email) > 7:
                if re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", email) != None:            
                    org_name = re.split(r'[@.]+', email)
                    if any("edu" in s for s in org_name):
                        return make_response(jsonify({'email':email, 'message':'you are an education institution, please contact our administrators for any help'}))
        
        return f(*args, **kwargs)
    return decorated
