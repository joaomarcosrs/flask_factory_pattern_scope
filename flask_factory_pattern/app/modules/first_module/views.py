from app.main import *


first_blueprint = Blueprint('first_blueprint', __name__, url_prefix=url_prefix)


#########################
#### Example View here ####
#########################
@first_blueprint.route('/example', methods=['GET'])
def example():
    return Response(json.dumps({'message': 'Success'}), mimetype='application/json', status=200)
