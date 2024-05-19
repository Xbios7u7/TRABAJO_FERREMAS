import json
from django.contrib.auth.models import User, Group

def create_users_and_groups_from_json():
    # Ruta al archivo JSON con los datos de los usuarios y grupos
    json_file_path = 'ferreApp/migrations/data.json'

    with open(json_file_path) as f:
        data = json.load(f)

    # Crear grupos
    for group_data in data['grupos']:
        group, _ = Group.objects.get_or_create(name=group_data['name'])

    # Crear usuarios y asignarlos a grupos
    for user_data in data['usuarios']:
        username = user_data['username']
        email = user_data['email']
        password = user_data['password']

        user, _ = User.objects.get_or_create(username=username, email=email)
        user.set_password(password)
        user.save()

        for group_data in data['grupos']:
            if username == group_data['name']:
                group = Group.objects.get(name=group_data['name'])
                user.groups.add(group)

if __name__ == '__main__':
    create_users_and_groups_from_json()
