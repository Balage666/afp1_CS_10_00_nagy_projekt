import os
import django
from users.models import User

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main.settings')
django.setup()

def create_users():
    user = User.objects.create_user(username='felhasznalo', password='jelszo', priv='0')
    user.save()

    admin = User.objects.create_user(username='admin', password='admin' priv='1')
    admin.save()

if __name__ == '__main__':
    create_users()
