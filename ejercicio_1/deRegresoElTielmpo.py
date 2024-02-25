import requests

def obtener_usuarios():
    url = 'https://jsonplaceholder.typicode.com/users'
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            print(f'Error al obtener datos: {response.status_code}')
            return None
    except Exception as e:
        print(f'Error de conexión: {e}')
        return None

def mostrar_usuarios(usuarios):
    if usuarios:
        print("Lista de usuarios:")
        for usuario in usuarios:
            print(f"ID: {usuario['id']}, Nombre: {usuario['name']}, Email: {usuario['email']}")
    else:
        print("No se pudo obtener la lista de usuarios")

if __name__ == "__main__":
    usuarios = obtener_usuarios()
    mostrar_usuarios(usuarios)
