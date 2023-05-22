# TODO
ToDo: Lista de teras

Ejemplo de como hacer una ToDo (Lista de tareas o pendientes) con django.


## Prerequisitos

Necesitamos instalar el pipenv como entorno virtual de trabajo.

```bash
pip install --user pipenv
```

En caso de no tener instalado el pip pueden usar el siguiente comando
```bash
sudo apt install python3-pip
```

## Realizar un copia del ejemplo

Realiza un git clone desde:

```bash
git clone https://github.com/Hacklibre-SAC/ToDo_List
cd ToDo_List
```

## Creación del entorno de trabajo

Para crear un entorno de trabajo solo debes de ingresar:

```bash
pipenv shell
pipenv install
```

## configuración de settings.py

Ingresar al settings.py y configura la base de datos que vas a usar `(está configurado para trabajar con postgresql)`, para mas ejemplos (https://docs.djangoproject.com/en/4.2/ref/settings/#databases)

### Migración de base de datos

Una vez configurado `settings.py` ingresa los siguientes comandos para crear las migraciones en base de datos

```bash
pipenv run python manage.py makemigrations
pipenv run python manage.py migrate
```
Luego, crea tu super-administrador

```bash
pipenv run python manage.py createsuperuser
```

Luego lanza el servidor local:

```bash
pipenv run python manage.py runserver
```

DISFRUTA!!!