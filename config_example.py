"""
    jumpserver.config
    ~~~~~~~~~~~~~~~~~

    Jumpserver project setting file

    :copyright: (c) 2014-2016 by Jumpserver Team.
    :license: GPL v2, see LICENSE for more details.
"""
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class Config:
    # Use it to encrypt or decrypt data
    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = os.environ.get('SECRET_KEY') or '2vym+ky!997d5kkcc64mnz06y1mmui3lut#(^wd=%s_qj$1%x'

    # How many line display every page if using django pager, default 25
    DISPLAY_PER_PAGE = 25

    # It's used to identify your site, When we send a create mail to user, we only know login url is /login/
    # But we should know the absolute url like: http://jms.jumpserver.org/login/, so SITE_URL is
    # HTTP_PROTOCOL://HOST[:PORT]
    SITE_URL = 'http://localhost'

    # Django security setting, if your disable debug model, you should setting that
    ALLOWED_HOSTS = ['*']

    # Development env open this, when error occur display the full process track, Production disable it
    DEBUG = True

    # DEBUG, INFO, WARNING, ERROR, CRITICAL can set. See https://docs.djangoproject.com/en/1.10/topics/logging/
    LOG_LEVEL = 'DEBUG'
    LOG_DIR = os.path.join(BASE_DIR, 'logs')

    # Database setting, Support sqlite3, mysql, postgres ....
    # See https://docs.djangoproject.com/en/1.10/ref/settings/#databases

    # SQLite setting:
    DB_ENGINE = 'sqlite3'
    DB_NAME = os.path.join(BASE_DIR, 'data', 'db.sqlite3')

    # MySQL or postgres setting like:
    # DB_ENGINE = 'mysql'
    # DB_HOST = '127.0.0.1'
    # DB_PORT = 3306
    # DB_USER = 'root'
    # DB_PASSWORD = ''
    # DB_NAME = 'jumpserver'

    # Use Redis as broker for celery and web socket
    REDIS_HOST = '127.0.0.1'
    REDIS_PORT = 6379
    REDIS_PASSWORD = ''
    BROKER_URL = 'redis://%(password)s%(host)s:%(port)s/3' % {
        'password': REDIS_PASSWORD,
        'host': REDIS_HOST,
        'port': REDIS_PORT,
    }

    # Api token expiration when create, Jumpserver refresh time when request arrive
    TOKEN_EXPIRATION = 3600

    # Session and csrf domain settings
    SESSION_COOKIE_AGE = 3600*24

    # Email SMTP setting, we only support smtp send mail
    EMAIL_HOST = 'smtp.163.com'
    EMAIL_PORT = 25
    EMAIL_HOST_USER = ''
    EMAIL_HOST_PASSWORD = ''  # Caution: Some SMTP server using `Authorization Code` except password
    EMAIL_USE_SSL = True if EMAIL_PORT == 465 else False
    EMAIL_USE_TLS = True if EMAIL_PORT == 587 else False
    EMAIL_SUBJECT_PREFIX = '[Jumpserver] '

    CAPTCHA_TEST_MODE = False

    # You can set jumpserver usage url here, that when user submit wizard redirect to
    USER_GUIDE_URL = ''

    # LDAP Auth settings
    AUTH_LDAP = False
    AUTH_LDAP_SERVER_URI = 'ldap://localhost:389'
    AUTH_LDAP_BIND_DN = 'cn=admin,dc=jumpserver,dc=org'
    AUTH_LDAP_BIND_PASSWORD = ''
    AUTH_LDAP_SEARCH_OU = 'ou=tech,dc=jumpserver,dc=org'
    AUTH_LDAP_SEARCH_FILTER = '(cn=%(user)s)'
    AUTH_LDAP_USER_ATTR_MAP = {
        "username": "cn",
        "name": "sn",
        "email": "mail"
    }
    AUTH_LDAP_START_TLS = False

    def __init__(self):
        pass

    def __getattr__(self, item):
        return None


config = {
    'default': Config,
}

env = 'default'
