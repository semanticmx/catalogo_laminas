# catalogo_laminas
Catálogo de Láminas por Cliente

# Instalación
git clone git@github.com:semanticmx/catalogo_laminas.git -b develop
pip install -r requirements.txt

# Configuración
* Actualizar la configuración de ALLOWED_HOSTS
* cambiar permisos a manage.py usando chmod 755 manage.py
* ./manage.py collectstatic

# Si es la primera vez que se instala el proyecto 
* ./manage.py makemigrations

# Actualizar Base de Datos 
* ./manage.py migrate

# Agregar usuario administrador
* ./manage.py createsuperuser

# Agregar nuevos modelos a la base de datos
* ./manage.py makemigrations <app> --name <accion>_<campo>
* ./manage.py migrate

# Referencias
Basado en https://docs.djangoproject.com/es/2.1/intro/tutorial01/
