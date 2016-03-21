from __future__ import unicode_literals
from django.apps import AppConfig

class ApiConfig(AppConfig):
    name = 'api'

    #Swagger documentation settings.
    SWAGGER_SETTINGS = {
        'exclude_namespaces': [],
        'api_version': '0.1',
        'api_path': '/',
        'enabled_methods': [
            'get',
            'post',
            'put',
            'patch',
            'delete'
        ],
        'api_key': '',
        'is_authenticated': False,
        'is_superuser': False,
        'unauthenticated_user': 'django.contrib.auth.models.AnonymousUser',
        'permission_denied_handler': None,
        'resource_access_handler': None,
        'info': {
            'contact': 'stathischaritos@gmail.com',
            'description': 'Sample BDD django project',
            'license': 'Apache 2.0',
            'title': 'Django - Behave - Swagger',
        },
        'doc_expansion': 'none',
    }