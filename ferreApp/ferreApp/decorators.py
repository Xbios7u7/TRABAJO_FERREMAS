# import json
# from django.contrib.auth.models import User, Group

# def create_users_and_groups_from_json():
#     # Ruta al archivo JSON con los datos de los usuarios y grupos
#     json_file_path = 'ferreApp/migrations/data.json'

#     try:
#         # Intenta abrir el archivo JSON y cargar sus datos
#         with open(json_file_path) as f:
#             # Lee el contenido del archivo y verifica si está vacío
#             data = f.read().strip()
#             if data:
#                 # Si el archivo no está vacío, intenta cargar los datos JSON
#                 data = json.loads(data)
#             else:
#                 # Si el archivo está vacío, imprime un mensaje y devuelve
#                 print("El archivo JSON está vacío.")
#                 return
#     except FileNotFoundError:
#         # Si el archivo no se encuentra, imprime un mensaje y devuelve
#         print("El archivo JSON no se encontró.")
#         return
#     except json.decoder.JSONDecodeError as e:
#         # Si hay un error al cargar el JSON, imprime el error y devuelve
#         print(f"Error al cargar el archivo JSON: {e}")
#         return

#     # Continúa con la lógica para crear usuarios y grupos a partir de los datos JSON
#     # ...

# if __name__ == '__main__':
#     create_users_and_groups_from_json()
# # Path: ferreApp/management/commands/create.py