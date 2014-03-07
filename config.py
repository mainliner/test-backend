SRF_ENABLED = True
SECRET_KEY = 'iwnids-sdf-sdfeg-erewr'


import os
basedir = os.path.abspath(os.path.dirname(__file__))

DBUSERNAME='root'
DBPASSWD='mainliner880320'
DBHOST='localhost'
DBNAME='ios_push'


SQLALCHEMY_DATABASE_URI = 'mysql://'+DBUSERNAME+':'+DBPASSWD+'@'+DBHOST+'/'+DBNAME
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir,'db_repository')
