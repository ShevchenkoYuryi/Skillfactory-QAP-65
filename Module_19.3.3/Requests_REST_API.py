import json

from PIL import Image

import requests


base_url = 'https://petstore.swagger.io/v2/'
status_code_list = []

# №4 GET /pet/findByStatus  Find pets by status
print('№4 GET /pet/findByStatus  Find pets by status')
status = 'available'    # задаем статус по котрому будем искать

res = requests.get(f"{base_url}pet/findByStatus?status={status}", headers={'accept': 'application/json'})
status_code_list.append(res.status_code)

print('Код статуса запроса:', res.status_code)
print('Ответ сервера', res.json())
print('---------------------------------------------------------------------------------------------------------------')


# №5 GET /pet/{petId}  Find pet by ID
print('№5 GET /pet/{petId}  Find pet by ID')

petId = res.json()[0]['id']    # определяем petId

res = requests.get(f"{base_url}pet/{petId}", headers={'accept': 'application/json'})
status_code_list.append(res.status_code)

print('Код статуса запроса:', res.status_code)
print('Ответ сервера', res.json())
print('---------------------------------------------------------------------------------------------------------------')


# №1 POST /pet/{petId}/uploadImage Uploads an image
print('№1 POST /pet/{petId}/uploadImage Uploads an image')

image = Image.open('img_1.jpg')
files = {'file': (image, open(image, 'rb'), 'image/jpeg')}

res = requests.post(f"{base_url}pet/{petId}/uploadImage", headers={'accept': 'application/json',
                                                                   'Content-Type': 'multipart/form-data'}, files=files)
status_code_list.append(res.status_code)

print('Код статуса запроса:', res.status_code)
print('Ответ сервера', res.json())
print('---------------------------------------------------------------------------------------------------------------')



# №6 POST /pet/{petId}  Updates a pet in the store with form data
print('№6 POST /pet/{petId}  Updates a pet in the store with form data')

res = requests.post(f"{base_url}pet/{petId}", headers={'accept': 'application/json'},
                    data={'name': 'pirat', 'status': 'sold'})
status_code_list.append(res.status_code)

print('Код статуса запроса:', res.status_code)
print('Ответ сервера', res.json())
print('-------------------------------------------------------------------------------------------------------------')





print(status_code_list)