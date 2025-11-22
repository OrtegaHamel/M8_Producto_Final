import os
import django


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gestion_musica.settings')
django.setup()

from django.contrib.auth.models import User

username = "root"
password = "root"
email = "r@root.com"

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, password=password, email=email)
    print("Superusuario creado")
else:
    print("Superusuario ya existe")
