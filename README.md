# EventsAPI
API destinada a brindar información para múltiples sistemas frontend, para el manejo de un sistema de control de órdenes de productos.

Para instalar la aplicación localmente:
* Crear Entorno Virtual
~~~
virtualenv env -p python3
~~~
* Instalar paquetes para el proyecto:
~~~
pip install -r requirements.txt
~~~
* Aplicar migraciones e iniciar el servidor:
~~~
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
~~~
