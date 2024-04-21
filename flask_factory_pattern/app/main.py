#### Create main imports here
import os
import re
import datetime
import time
import decimal
from pathlib import Path
from urllib.parse import urljoin, urlencode, urlparse, urlunparse
from collections import namedtuple, defaultdict
from datetime import date 
from dotenv import load_dotenv
from flask import jsonify, request, Blueprint, Response, json, current_app
from .models import db


#Provisory until define version
url_prefix = '/api/v1'

### Here you can define any class, function or 
### method that will be inherited by other modules. 
### Be careful with redundancy.

def db_add(obj):
    return db.session.add(obj)

def db_delete(obj):
    return db.session.delete(obj)
    
def db_excute(obj):
    return db.session.execute(obj)

def db_query(obj):
    return db.session.query(obj)
    
def db_commit():
    return db.session.commit()

def db_flush():
    return db.session.flush()

