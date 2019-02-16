# catalogo_laminas
Catálogo de Láminas por Cliente

# Configuración
* Actualizar la configuración de ALLOWED_HOSTS
* cambiar permisos a manage.py usando chmod 755 manage.py
* ./manage.py collectstatic

# Actualizar Base de Datos 
* ./manage.py migrate

# Agregar nuevos modelos a la base de datos
* ./manage.py makemigrations <app> --name <accion>_<campo>
* ./manage.py migrate

# Agregar usuario administrador
* ./manage.py createsuperuser

# Referencias
Basado en https://docs.djangoproject.com/es/2.1/intro/tutorial01/
