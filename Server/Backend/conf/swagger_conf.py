SWAGGER_SETTINGS = {
    'LOGIN_URL': 'rest_framework:login',
    'LOGOUT_URL': 'rest_framework:logout'
}

# drf-yasg 配置
SWAGGER_SETTINGS = {
    'USE_SESSION_AUTH': True,
    'api_version': '1.0',
    'enabled_methods': ['get', 'post', 'put', 'patch', 'delete'],
    'SECURITY_DEFINITIONS': {
        'basic': {
            'type': 'basic',
        },
    },
}
