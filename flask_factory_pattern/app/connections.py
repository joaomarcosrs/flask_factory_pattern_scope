import os
import requests
import smtplib
import pymssql
from flask import jsonify


### Create some connections here

def connection_smtp():
    try:
        smtp_server = os.environ.get('SMTP_SERVER')
        smtp_port = os.environ.get('SMTP_PORT')
        smtp_user = os.environ.get('SMTP_USER')
        smtp_pwd = os.environ.get('SMTP_PWD')
        
        smtp = smtplib.SMTP(smtp_server, smtp_port)
        # identify ourselves to smtp gmail client
        smtp.ehlo()
        # secure our email with tls encryption
        smtp.starttls()
        # re-identify ourselves as an encrypted connection
        smtp.ehlo()
        smtp.login(smtp_user, smtp_pwd)
        return smtp, smtp_user
    
    except ConnectionError:
        return jsonify('Could not connect to smtp server!')

