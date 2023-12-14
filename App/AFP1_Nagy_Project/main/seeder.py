import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main.settings')
django.setup()

from django.contrib.auth.models import User

users_data = [
    {'username': 'felhasznalo', 'first_name': 'Elek', 'last_name': 'Vicc', 'email': 'viccelek@example.com', 'password': 'jelszo'},
    {'username': 'imi', 'first_name': 'Imre', 'last_name': 'Fütty', 'email': 'futtyimre@example.com', 'password': 'password'},
    {'username': 'admin', 'first_name': 'Admin', 'last_name': 'Admin', 'email': 'admin@example.com', 'password': 'admin', 'is_superuser': True},
]

try:
    for data in users_data:
        is_superuser = data.pop('is_superuser', False)
        user = User.objects.create_user(**data)
        if is_superuser:
            user.is_superuser = True
            user.save()
except Exception as e:
    print(f'Hiba történt az adatok feltöltésekor: {e}')
else:
    print('Az adatok már feltöltve')
