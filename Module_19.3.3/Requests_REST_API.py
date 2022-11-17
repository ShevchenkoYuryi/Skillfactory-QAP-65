import json

import settings
import requests
from datetime import datetime, timezone


base_url = 'https://petstore.swagger.io/v2/'
status_code_list = []  # создаем словари для коллекции кодов ответа
status_code_list_store = []
status_code_list_user = []

# №2 POST /pet Add a new pet to the store
print('№2 POST /pet Add a new pet to the store')

data = settings.body
data['name'] = 'pirats'
data = json.dumps(data)

res = requests.post(f"{base_url}pet", headers={'accept': 'application/json', 'Content-Type': 'application/json'}, data=data)
status_code_list.append(res.status_code)
petId = res.json()['id']  # сохраняем в переменную id созданного питомца для последующей работы именно с ним

print('Код статуса запроса:', res.status_code)
print('Ответ сервера', res.json())
print('-----------------------------------\n')

# Я НЕ ЗНАЮ ПОЧЕМУ ОН НЕРАБОТАЕТ
# №1 POST /pet/{petId}/uploadImage Uploads an image
print('№1 POST /pet/{petId}/uploadImage Uploads an image')

image = 'cats.jpg'
files = {'file': (image, open(image, 'rb'), 'image/jpeg')}

res = requests.post(f"{base_url}pet/{petId}/uploadImage", headers={'accept': 'application/json',
                                                                   'Content-Type': 'multipart/form-data'}, files=files)
status_code_list.append(res.status_code)

print('Код статуса запроса:', res.status_code)
print('Ответ сервера', res.json())
print('-----------------------------------\n')


# №3 PUT /pet Update an existing pet
print('№3 PUT /pet Update an existing pet')

data = settings.body
data['id'] = petId  # перезаписываем переменную что бы продолжать работать с созданным нами питомцем
data['name'] = 'Shrec'
data['category']['name'] = "Ogr"
data['status'] = 'pending'
data = json.dumps(data)

res = requests.put(f"{base_url}pet", headers={'accept': 'application/json', 'Content-Type': 'application/json'}, data=data)
status_code_list.append(res.status_code)

print('Код статуса запроса:', res.status_code)
print('Ответ сервера', res.json())
print('-----------------------------------\n')


# №4 GET /pet/findByStatus  Find pets by status
print('№4 GET /pet/findByStatus  Find pets by status')
status = 'available'    # задаем статус по котрому будем искать

res = requests.get(f"{base_url}pet/findByStatus?status={status}", headers={'accept': 'application/json'})
status_code_list.append(res.status_code)
id_by_status = res.json()[0]['id']

print('Код статуса запроса:', res.status_code)
print('Ответ сервера', res.json())
print('-----------------------------------\n')
#
#
# # №5 GET /pet/{petId}  Find pet by ID
# print('№5 GET /pet/{petId}  Find pet by ID')
#
# res = requests.get(f"{base_url}pet/{petId}", headers={'accept': 'application/json'})
# status_code_list.append(res.status_code)
#
# print('Код статуса запроса:', res.status_code)
# print('Ответ сервера', res.json())
# print('-----------------------------------\n')
#
#
# # №6 POST /pet/{petId}  Updates a pet in the store with form data
# print('№6 POST /pet/{petId}  Updates a pet in the store with form data')
#
# res = requests.post(f"{base_url}pet/{petId}", headers={'accept': 'application/json'}, data={'name': 'pirat', 'status': 'sold'})
# status_code_list.append(res.status_code)
#
# print('Код статуса запроса:', res.status_code)
# print('Ответ сервера', res.json())
# print('-----------------------------------\n')
#
#
# # №7 DELETE /pet/{petId}  Deletes a pet
# print('DELETE /pet/{petId}  Deletes a pet')
#
# res = requests.delete(f"{base_url}pet/{petId}", headers={'accept': 'application/json'})
# status_code_list.append(res.status_code)
#
# print('Код статуса запроса:', res.status_code)
# print('Ответ сервера', res.json())
# print('-----------------------------------\n')
#


# №8 POST /user Create user
print('№8 POST /user Create user')

user = settings.create_user
user = json.dumps(user)

res = requests.post(f"{base_url}user", headers={'accept': 'application/json', 'Content-Type': 'application/json'},
                    data=user)
status_code_list_user.append(res.status_code)

print('Код статуса запроса:', res.status_code)
print('Ответ сервера', res.json())
print('-----------------------------------\n')


# №9 PUT /user/{username} Updated user object
print('№9 PUT /user/{username} Updated user object')

username = settings.create_user['username']
new_user = settings.update_user
new_user = json.dumps(new_user)

res = requests.put(f"{base_url}user/{username}", headers={'accept': 'application/json', 'Content-Type': 'application/json'},
                    data=new_user)
status_code_list_user.append(res.status_code)
user_id = res.json()['message']
print(user_id)

print('Код статуса запроса:', res.status_code)
print('Ответ сервера', res.json())
print('-----------------------------------\n')


# №10 GET/user/login Logs user into the system
print('№10 GET/user/login Logs user into the system')

username = settings.update_user['username']
password = settings.update_user["password"]
new_user = json.dumps(new_user)

res = requests.get(f"{base_url}user/login?username={username}&password{password}", headers={'accept': 'application/json'})
status_code_list_user.append(res.status_code)
user_session = res.json()['message']

print('Код статуса запроса:', res.status_code)
print('Ответ сервера', res.json())
print('-----------------------------------\n')


# №12 GET/user/{username} Get user by user name
print('№12 GET/user/{username} Get user by user name')

username = settings.update_user['username']

res = requests.get(f"{base_url}user/{username}", headers={'accept': 'application/json'})
status_code_list_user.append(res.status_code)

print('Код статуса запроса:', res.status_code)
print('Ответ сервера', res.json())
print('-----------------------------------\n')


# №13 POST /user/createWithArray Creates list of users with given input array
print('№13 POST /user/createWithArray Creates list of users with given input array')

user = settings.list_u
user = json.dumps(user)

res = requests.post(f"{base_url}user/createWithArray", headers={'accept': 'application/json', 'Content-Type': 'application/json'},
                    data=user)
status_code_list_user.append(res.status_code)

print('Код статуса запроса:', res.status_code)
print('Ответ сервера', res.json())
print('-----------------------------------\n')


# №14 POST /user/createWithList Creates list of users with given input array
print('№14 POST /user/createWithList Creates list of users with given input array')

user = settings.list_u
user = json.dumps(user)

res = requests.post(f"{base_url}user/createWithList", headers={'accept': 'application/json', 'Content-Type': 'application/json'},
                    data=user)
status_code_list_user.append(res.status_code)

print('Код статуса запроса:', res.status_code)
print('Ответ сервера', res.json())
print('-----------------------------------\n')


# №15 DELETE /user/{username} Delete user
print('15 DELETE /user/{username} Delete user')

user = settings.update_user['username']

res = requests.delete(f"{base_url}user/{username}", headers={'accept': 'application/json'})
status_code_list_user.append(res.status_code)

print('Код статуса запроса:', res.status_code)
print('Ответ сервера', res.json())
print('-----------------------------------\n')


# №11 GET/user/logout Logs out current logged in user session
print('№11 GET/user/logout Logs out current logged in user session')

res = requests.get(f"{base_url}user/logout", headers={'accept': 'application/json'})
status_code_list_user.append(res.status_code)

print('Код статуса запроса:', res.status_code)
print('Ответ сервера', res.json())
print('-----------------------------------\n')


# №16 POST /store/order Place an order for a pet
print('№16 POST /store/order Place an order for a pet')

today = datetime.now(timezone.utc)
order = settings.body_order
order['shipDate'] = today.isoformat()
order = json.dumps(order)

res = requests.post(f"{base_url}store/order", headers={'accept': 'application/json', 'Content-Type': 'application/json'},
                    data=order)

orderId = res.json()["id"]
status_code_list_store.append(res.status_code)

print('Код статуса запроса:', res.status_code)
print('Ответ сервера', res.json())
print('-----------------------------------\n')


# №17 GET /store/order/{orderId} Find purchase order by ID
print('№17 GET /store/order/{orderId} Find purchase order by ID')

res = requests.get(f"{base_url}store/order/{orderId}", headers={'accept': 'application/json'})

status_code_list_store.append(res.status_code)

print('Код статуса запроса:', res.status_code)
print('Ответ сервера', res.json())
print('-----------------------------------\n')


# №18 GET /store/inventory Returns a map of status codes to quantities
print('№18 GET /store/inventory Returns a map of status codes to quantities')

res = requests.get(f"{base_url}store/inventory", headers={'accept': 'application/json'})

status_code_list_store.append(res.status_code)

print('Код статуса запроса:', res.status_code)
print('Ответ сервера', res.json())
print('-----------------------------------\n')


# №19 DELETE /store/order/{orderId} Delete purchase order by ID
print('№19 DELETE /store/order/{orderId} Delete purchase order by ID')

res = requests.delete(f"{base_url}store/order/{orderId}", headers={'accept': 'application/json'})

status_code_list_store.append(res.status_code)

print('Код статуса запроса:', res.status_code)
print('Ответ сервера', res.json())
print('-----------------------------------\n')


print('Стутс коды по коллекции "Everything about your Pets":\n', *status_code_list, '\n')
print('Стутс коды по коллекции "Operations about user":\n', *status_code_list_user, '\n')
print('Стутс коды по коллекции "Access to Petstore orders":\n', *status_code_list_store, '\n')




