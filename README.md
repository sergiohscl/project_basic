# Projeto Django Básico
## Objetivo do projeto e implementar conceitos básicos, como:
#### Criar tela de login e cadastro;
#### Criar login social (google);
#### Criar Home para enviar um formulario;
#### Criar navbar com avatar se existir;
#### Criar mensagens de sucessos e erros;
#### Implementar o signals para disparar email de boas vindas;
#### Criar conexão com DB em mysql;
#### Criar script com dados fake para popular o DB;
#### Criar apis usando DRF;
#### Implementar o swagger;
#### Criar testes usando testCase e o APITestCase do DRF; 

<hr>

## Documentação do django
https://www.djangoproject.com/

## Instalando ambiente virtual
    python3 -m venv venv

## Ativando e desativando ambiente virtual
### Linux
    . venv/bin/activate
    deactivate

### Windows
    source venv\Scripts\Activate.ps1   # terminal powersheel        
    source venv\Scripts\Activate.bat   # terminal cmd

## Instalando django no ambiente virtual
    pip install django

## Iniciando project django
    django-admin startproject <nome-project> .

## Criar o arquivo requirements.txt
    pip freeze > requirements.txt

## Instale as dependências no projeto
    pip install -r requirements.txt

## Rodando django-admin
    python manage.py runserver

## Migrando a base de dados do Django
    python manage.py makemigrations
    python manage.py migrate

## Criando e modificando a senha de um super usuário
    python manage.py createsuperuser
    python manage.py changepassword USERNAME

# configure settings
## imports
    import os
    from django.contrib.messages import constants

## templates   
    TEMPLATES = 'DIRS': [os.path.join(BASE_DIR, 'templates')]

## language e timezone
    LANGUAGE_CODE = "pt-BR"
    TIME_ZONE = "America/Sao_Paulo"

## static files:
    STATICFILES_DIRS = (os.path.join(BASE_DIR, 'templates/static'),)

    STATIC_ROOT = os.path.join('static')

    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
    MEDIA_URL = '/media/'

## Django message
    MESSAGE_TAGS = {
        constants.DEBUG: 'alert-primary',
        constants.ERROR: 'alert-danger',
        constants.SUCCESS: 'alert-success',
        constants.INFO: 'alert-info',
        constants.WARNING: 'alert-warning',
    }

## configurar urls
    from django.conf import settings
    from django.conf.urls.static import static

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

## Configurar o git
    git config --global user.name 'Seu nome'
    git config --global user.email 'seu_email@gmail.com'
    git config --global init.defaultBranch main
    git init
    git add .
    git commit -m 'Mensagem'
    git remote add origin URL_DO_GIT

## criando app
    python manage.py startapp <nomeapp>

## Settings Auth User Model - abaixo do database
    AUTH_USER_MODEL = "<nomeapp>.CustomUser"

## Install Pillow
    pip install Pillow

## biblioteca para pegar informações do .env
    pip install python-decouple

## Install fake
    pip install Faker

## Install pymsql
    pip install pymysql

## rodando script para inserir dados fakes
    python3 utils/data_livros.py

## configuração do email no settings
    # Email
    DEFAULT_FROM_EMAIL = 'sergiohscl2@gmail.com'
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST_USER = config('EMAIL_HOST_USER')
    EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
    EMAIL_USE_TLS = config('EMAIL_USE_TLS')
    EMAIL_PORT = config('EMAIL_PORT')
    EMAIL_HOST = config('EMAIL_HOST')

## login social (google)
https://umcodigo.com/autenticacao-com-google-no-django/

## DRF - Django Rest-Framework
    REST_FRAMEWORK = {
        'DEFAULT_AUTHENTICATION_CLASSES': (
            # 'rest_framework.authentication.SessionAuthentication',
            'rest_framework.authentication.TokenAuthentication',
        ),
        'DEFAULT_PERMISSION_CLASSES': (
            'rest_framework.permissions.IsAuthenticatedOrReadOnly',
        ),
        'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',  # noqa E501
        'PAGE_SIZE': 2,
        'DEFAULT_THROTTLE_CLASSES': (
            'rest_framework.throttling.AnonRateThrottle',
            'rest_framework.throttling.UserRateThrottle',
        ),
        'DEFAULT_THROTTLE_RATES': {
            'anon': '5/minute',  # second, day, month, year
            'user': '10/minute',
        }
    }

## settings DRF
    INSTALLED_APPS = [
        'drf_yasg',
        'django_filters',
        'rest_framework',
        'rest_framework.authtoken',
    ]

## install drf e filters
    pip install drf-yasg
    pip install django-filter

## Implemente o swagger no settings
    SWAGGER_SETTINGS = {
        'USE_SESSION_AUTH': False,
        'SECURITY_DEFINITIONS': {
            "api_key": {
                "type": "apiKey",
                "name": "Authorization",
                "in": "header"
            },
        }
    }

## implemente swagger arquivo urls 
    schema_view = get_schema_view(
        openapi.Info(
            title="Snippets API",
            default_version='v1',
            description="Test description",
            terms_of_service="https://www.google.com/policies/terms/",
            contact=openapi.Contact(email="contact@snippets.local"),
            license=openapi.License(name="BSD License"),
        ),
        public=True,
        permission_classes=(permissions.DjangoModelPermissions,),
    )

## import bibliotecas urls - swagger e drf
    from rest_framework import permissions
    from drf_yasg.views import get_schema_view
    from drf_yasg import openapi

## configure url - swagger
    urlpatterns = [
        path('swagger<format>/', schema_view.without_ui(cache_timeout=0),name='schema-json'),
        path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
        path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    ]

## Rodando os testes
    python manage.py test <nome app>/tests
