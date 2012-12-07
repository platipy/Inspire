from flask import jsonify, request

def json_error(error, *args, **kwargs):
    if args:
        return jsonify(type="error", error=error, data=args)
    return jsonify(type="error", error=error, data=kwargs)
    
def json_success(*args, **kwargs):
    if args:
        return jsonify(type="success", data=args)
    return jsonify(type="success", data=kwargs)
    
# I think I got rid of this, but I don't remember
def check_request_arguments(*args):
    return not all(item in request.args.keys() for item in args)
    