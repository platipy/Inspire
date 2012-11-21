from flask import jsonify, request

def json_error(error, **kwargs):
    return jsonify(type="error", error=error, data=kwargs)
    
def json_success(**kwargs):
    return jsonify(type="success", data=kwargs)
    
def check_request_arguments(*args):
    return not all(item in request.args.keys() for item in args)
    