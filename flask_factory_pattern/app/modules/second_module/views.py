from app.main import *


second_blueprint = Blueprint('second_blueprint', __name__, url_prefix=url_prefix)


@second_blueprint.route('/second_example', methods=['GET'])
def second_example_get():
    return Response(json.dumps({'message': 'Success'}), mimetype='application/json', status=200)