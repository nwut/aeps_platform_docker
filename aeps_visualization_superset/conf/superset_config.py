import os

#MAPBOX_API_KEY = os.getenv('MAPBOX_API_KEY', '')
MAPBOX_API_KEY = 'pk.eyJ1Ijoic3RldmVuY2lhdCIsImEiOiJjancyYW5scnQwdXNkNDRsMnRoYncwdmVtIn0.T5qcZBJenj5JHVgWqFyP9g'
#CACHE_CONFIG = {
#    'CACHE_TYPE': 'redis',
#    'CACHE_DEFAULT_TIMEOUT': 300,
#    'CACHE_KEY_PREFIX': 'superset_',
#    'CACHE_REDIS_HOST': 'redis',
#    'CACHE_REDIS_PORT': 6379,
#    'CACHE_REDIS_DB': 1,
#    'CACHE_REDIS_URL': 'redis://redis:6379/1'}
SQLALCHEMY_DATABASE_URI = 'mysql://aeps_user:your_password@172.17.0.3:3306/aeps_2_0'
SQLALCHEMY_TRACK_MODIFICATIONS = True
SECRET_KEY = 'thisISaSECRET_1234'
HTTP_HEADERS = {'X-Frame-Options': 'ALLOWALL'}
