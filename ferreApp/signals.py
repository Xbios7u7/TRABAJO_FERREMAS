

import json
from django.contrib.auth.models import User, Group
from django.db.models.signals import post_migrate
from django.dispatch import receiver

@receiver(post_migrate)
def create_groups_and_users(sender, **kwargs):
    # Lógica para crear grupos después de las migraciones
    groups = ['bodeguero', 'vendedor', 'contador', 'administrador']
    for group_name in groups:
        Group.objects.get_or_create(name=group_name)

    # Lógica para crear usuarios después de las migraciones
    users = [
        {'username': 'bodeguero', 'email': 'bodeguero@example.com', 'password': '11111111-3'},
        {'username': 'vendedor', 'email': 'vendedor@example.com', 'password': '11111111-3'},
        {'username': 'contador', 'email': 'contador@example.com', 'password': '11111111-3'},
        {'username': 'administrador', 'email': 'administrador@example.com', 'password': '11111111-3'}
    ]
    for user_data in users:
        user, created = User.objects.get_or_create(
            username=user_data['username'],
            email=user_data['email'],
        )
        if created:
            user.set_password(user_data['password'])
            user.save()

        # Asignar usuarios a grupos
        group = Group.objects.get(name=user_data['username'])
        user.groups.add(group)
        user.save()

    # Serializar todos los datos de usuarios y grupos a JSON
    all_users = list(User.objects.values('username', 'email', 'password'))
    all_groups = list(Group.objects.values('name'))

    # Guardar todos los datos en el archivo JSON
    json_file_path = 'ferreApp/migrations/data.json'
    existing_data = {'usuarios': all_users, 'grupos': all_groups}
    with open(json_file_path, 'w') as f:
        json.dump(existing_data, f, indent=4)

