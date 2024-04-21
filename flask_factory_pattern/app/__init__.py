from flask import Flask
from flask.cli import load_dotenv
from flask_cors import CORS
from flask_migrate import Migrate
from flask_swagger_ui import get_swaggerui_blueprint
from .db import set_basic_config_db


migrate = Migrate()

def create_app():
    app = Flask(__name__)
    load_dotenv(".env")
    
    app.config.from_object('config.Config')
    CORS(app)
    
    SWAGGER_URL = '/swagger'
    API_URL = '/static/swagger.json'
    SWAGGER_BLUEPRINT = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL,
        config={
            'app_name': 'API Documentation'
        }
    )
    
    from .models import db
    db.init_app(app)
    migrate.init_app(app, db)
    
    with app.app_context():
        db.create_all()
        set_basic_config_db(db)
        
        #Importing blueprints
        from .modules.first_module.views import first_blueprint
        from .modules.second_module.views import second_blueprint
        from .modules.third_module.views import third_blueprint
        
        #Blueprints
        app.register_blueprint(first_blueprint)
        app.register_blueprint(second_blueprint)
        app.register_blueprint(third_blueprint)
        app.register_blueprint(SWAGGER_BLUEPRINT, url_prefix=SWAGGER_URL)
    
    return app

