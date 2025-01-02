# Importando as bibliotecas necessárias
import requests

# URL base para a API JSONPlaceholder
base_url = "https://jsonplaceholder.typicode.com"

# Usando GET para obter informações sobre posts
get_url = f"{base_url}/posts/1"
response_get = requests.get(get_url)
print("GET Response:", response_get.json())

# Usando POST para criar um novo post
post_url = f"{base_url}/posts"
post_data = {
    'title': 'foo',
    'body': 'bar',
    'userId': 1
}
response_post = requests.post(post_url, data=post_data)
print("POST Response:", response_post.json())

# Usando PUT para atualizar um post existente completamente
put_url = f"{base_url}/posts/1"
put_data = {
    'id': 1,
    'title': 'Updated Title',
    'body': 'Updated Body',
    'userId': 1
}
response_put = requests.put(put_url, data=put_data)
print("PUT Response:", response_put.json())

# Usando PATCH para aplicar uma atualização parcial a um post
patch_url = f"{base_url}/posts/1"
patch_data = {
    'title': 'Partially Updated Title'
}
response_patch = requests.patch(patch_url, data=patch_data)
print("PATCH Response:", response_patch.json())

# Usando DELETE para deletar um post
delete_url = f"{base_url}/posts/1"
response_delete = requests.delete(delete_url)
print("DELETE Response Status Code:", response_delete.status_code)