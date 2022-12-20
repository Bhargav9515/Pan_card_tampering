import os
from os import environ

class config(object):
    
    DEBUG = False
    TESTING = False
    
    basedir = os.path.abspath(os.dirname(__file__))
    
    SECRET_KEY = 'ABK'
    
    UPLOADS = "D:\PAN-CARD-TEMPERING"
    
    SESSION_COOCKIE_SECURE = True
    DEFAULT_THEME = None
    
    class DevelopementConfig(Config):    
        DEBUG = True
        SESSION_COOCKIE_SECURE = False
        
    class DebugConfig(config):
        DEBUG = False