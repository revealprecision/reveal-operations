import os

from flask_appbuilder.security.manager import AUTH_OAUTH
from superset_patchup.oauth import CustomSecurityManager

from cachelib import RedisCache

ENABLE_PROXY_FIX = True
URL_PREFIX = 'https'
PREFERRED_URL_SCHEME = 'https'
ENABLE_CORS = True
CORS_OPTIONS = {
  "origins": "*",
  "methods": "GET,POST",
  "allow_headers": "Custom-Api-Token",
  "supports_credentials": True
}
SESSION_COOKIE_SAMESITE = None
SESSION_COOKIE_SECURE = True
SESSION_COOKIE_HTTPONLY = False
SUPERSET_WEBSERVER_TIMEOUT = 60
WTF_CSRF_ENABLED = False
WTF_CSRF_EXEMPT_LIST = ['login', 'superset.csrf_token',]
WTF_CSRF_TIME_LIMIT = 60 * 60 * 24 * 365

MAPBOX_API_KEY = os.getenv('MAPBOX_API_KEY', '')
CACHE_CONFIG = {
    'CACHE_TYPE': 'redis',
    'CACHE_DEFAULT_TIMEOUT': 300,
    'CACHE_KEY_PREFIX': 'superset_',
    'CACHE_REDIS_HOST': 'redis',
    'CACHE_REDIS_PORT': 6379,
    'CACHE_REDIS_DB': 1,
    'CACHE_REDIS_URL': 'redis://redis:6379/1'}
SQLALCHEMY_DATABASE_URI = \
    'postgresql+psycopg2://superset:not_so_secret@postgresql:5432/superset'
SQLALCHEMY_TRACK_MODIFICATIONS = True
SECRET_KEY = 'not_so_secret'

class CeleryConfig(object):
    BROKER_URL = 'redis://redis:6379/0'
    CELERY_IMPORTS = ('superset.sql_lab', )
    CELERY_RESULT_BACKEND = 'redis://redis:6379/0'
    CELERY_ANNOTATIONS = {'tasks.add': {'rate_limit': '10/s'}}

CELERY_CONFIG = CeleryConfig
RESULTS_BACKEND = RedisCache(
    host='redis',
    port=6379,
    key_prefix='superset_results'
)

AUTH_TYPE = AUTH_OAUTH

OAUTH_PROVIDERS = [
    {
        'name': 'opensrp',
        'icon': 'fa-address-card',
        'token_key': 'access_token',
        'remote_app': {
            'client_id': 'superset-server',
            'client_secret': 'aa54b492-a626-4591-8258-0290a0fcfd53',
            'client_kwargs':{
              'scope': 'openid email profile'
            },
            'request_token_url': None,
            'base_url': 'https://opensrp-dev.akros.online/opensrp/',
            'access_token_url': 'https://sso-dev.akros.online/auth/realms/reveal/protocol/openid-connect/token',
            'authorize_url': 'https://sso-dev.akros.online/auth/realms/reveal/protocol/openid-connect/auth',
            'user-details': 'https://opensrp-dev.akros.online/opensrp/user-details'
        }
    }
]


# Will allow user self registration
AUTH_USER_REGISTRATION = True
AUTH_USER_REGISTRATION_ROLE = 'Gamma'
OPENSRP_BASE_USER = 'https://opensrp-dev.akros.online/opensrp/user-details'
CUSTOM_SECURITY_MANAGER = CustomSecurityManager
