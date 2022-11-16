import json

from PIL import Image
import settings
import requests


base_url = 'https://petstore.swagger.io/v2/'
status_code_list = []  # создаем словари для коллекции кодов ответа
status_code_list_store = []
status_code_list_user = []

# # №2 POST /pet Add a new pet to the store
# print('№2 POST /pet Add a new pet to the store')
#
# data = settings.body
# data['name'] = 'pirats'
# data = json.dumps(data)
#
# res = requests.post(f"{base_url}pet", headers={'accept': 'application/json', 'Content-Type': 'application/json'}, data=data)
# status_code_list.append(res.status_code)
# petId = res.json()['id']  # сохраняем в переменную id созданного питомца для последующей работы именно с ним
#
# print('Код статуса запроса:', res.status_code)
# print('Ответ сервера', res.json())
# print('-----------------------------------\n')
#
#
# # №1 POST /pet/{petId}/uploadImage Uploads an image
# print('№1 POST /pet/{petId}/uploadImage Uploads an image')
#
# image = 'img_1.jpg'
# files = {'file': (image, open(image, 'rb'), 'image/jpeg')}
#
# res = requests.post(f"{base_url}pet/{petId}/uploadImage", headers={'accept': 'application/json',
#                                                                    'Content-Type': 'multipart/form-data'}, files=files)
# status_code_list.append(res.status_code)
#
# print('Код статуса запроса:', res.status_code)
# print('Ответ сервера', res.json())
# print('-----------------------------------\n')
#
#
# # №3 PUT /pet Update an existing pet
# print('№3 PUT /pet Update an existing pet')
#
# data = settings.body
# data['id'] = petId  # перезаписываем переменную что бы продолжать работать с созданным нами питомцем
# data['name'] = 'Shrec'
# data['category']['name'] = "Ogr"
# data['status'] = 'pending'
# data = json.dumps(data)
#
# res = requests.put(f"{base_url}pet", headers={'accept': 'application/json', 'Content-Type': 'application/json'}, data=data)
# status_code_list.append(res.status_code)
#
# print('Код статуса запроса:', res.status_code)
# print('Ответ сервера', res.json())
# print('-----------------------------------\n')
#
#
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
# print('Стутс коды по коллекции "Everything about your Pets":\n', *status_code_list, '\n')


# №8 POST /user Create user
print('№8 POST /user Create user')

user = settings.сreate_user
user = json.dumps(user)

res = requests.post(f"{base_url}user", headers={'accept': 'application/json', 'Content-Type': 'application/json'},
                    data=user)
status_code_list_user.append(res.status_code)

print('Код статуса запроса:', res.status_code)
print('Ответ сервера', res.json())
print('-----------------------------------\n')


# №9 PUT /user/{username} Updated user object
print('№9 PUT /user/{username} Updated user object')

username = settings.сreate_user['username']
new_user = settings.update_user
new_user = json.dumps(new_user)

res = requests.put(f"{base_url}user/{username}", headers={'accept': 'application/json', 'Content-Type': 'application/json'},
                    data=new_user)
status_code_list_user.append(res.status_code)
user_id = res.json()['message']

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


# №11 GET/user/logout Logs out current logged in user session
print('№10 GET/user/login Logs user into the system')

res = requests.get(f"{base_url}user/logout", headers={'accept': 'application/json'})
status_code_list_user.append(res.status_code)

print('Код статуса запроса:', res.status_code)
print('Ответ сервера', res.json())
print('-----------------------------------\n')









print('Стутс коды по коллекции "Operations about user":\n', *status_code_list_user, '\n')





# № POST /store/order Place an order for a pet
print('№8 POST /store/order Place an order for a pet')

order = settings.body_order
order['petId'] = id_by_status   # берем ID из запроса по статусу. Созданный нами питомец удалем => его ID тоже
order['quantity'] = 1
order['shipDate'] = '29/02/2022T12:00:01'
order = json.dumps(order)

res = requests.post(f"{base_url}store/order", headers={'accept': 'application/json', 'Content-Type': 'application/json'},
                    data=order)
status_code_list_store.append(res.status_code)

print('Код статуса запроса:', res.status_code)
print('Ответ сервера', res.json())
print('-----------------------------------\n')



print('Стутс коды по коллекции "Access to Petstore orders":\n', *status_code_list_store, '\n')