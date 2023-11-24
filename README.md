# Documentação do django
https://www.djangoproject.com/

# Instalando ambiente virtual
python3 -m venv venv

# Ativando e desativando ambiente virtual
. venv/bin/activate
deactivate

    ## windows
        source venv\Scripts\Activate.ps1   # terminal powersheel        
        source venv\Scripts\Activate.bat   # terminal cmd

# Instalando django no ambiente virtual
pip install django

# Iniciando project django
django-admin startproject project .

# Criar o arquivo requirements.txt
pip freeze > requirements.txt

# Instale as dependências no projeto
pip install -r requirements.txt

# Rodando django-admin
python manage.py runserver

# Migrando a base de dados do Django
python manage.py makemigrations
python manage.py migrate

# Criando e modificando a senha de um super usuário
python manage.py createsuperuser
python manage.py changepassword USERNAME

# configure settings template, arquivo estático e messages.
    import os
    from django.contrib.messages import constants
    INSTALLED_APPS = <nome do app>
    TEMPLATES = 'DIRS': [os.path.join(BASE_DIR, 'templates')]
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

# configurar urls
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Configurar o git
git config --global user.name 'Seu nome'
git config --global user.email 'seu_email@gmail.com'
git config --global init.defaultBranch main
git init
git add .
git commit -m 'Mensagem'
git remote add origin URL_DO_GIT

# criando app
python manage.py startapp <nomeapp>

# Settings Auth User Model - abaixo do database
AUTH_USER_MODEL = "<nomeapp>.CustomUser"

# Install Pillow
pip install Pillow

# biblioteca para pegar informações do .env
pip install python-decouple

# Install fake
pip install Faker

# Install pymsql
pip install pymysql

# rodando script para inserir dados fakes
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

    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
