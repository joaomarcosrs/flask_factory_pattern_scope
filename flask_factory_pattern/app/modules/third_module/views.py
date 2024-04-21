from app.main import *


third_blueprint = Blueprint('third_blueprint', __name__, url_prefix=url_prefix)


@third_blueprint.route('/third_example', methods=['POST'])
def institutions():
    if request.method == 'POST':
        return Response(json.dumps({'message': 'Success!'}), mimetype='application/json', status=201)
