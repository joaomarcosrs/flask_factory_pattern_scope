import tomli
from pathlib import Path
from .models import ExampleModel


def get_tomli_db():
    database = tomli.loads(Path('metadata.toml').read_text(encoding='utf 8'))['database']
    
    return database

def set_basic_config_db(db):
    
    database = get_tomli_db()
    
    default = ExampleModel.query.filter(ExampleModel.name == database['initial']['name']).first()
    
    if not default:
        set_default = ExampleModel(
            name=database['initial']['name'],
            description=database['initial']['description']
        )
        
        db.session.add(set_default)
        db.session.commit()