import json

with open('responce.json', encoding='utf8') as file:
    respfile = file.load(file)

with open('test.txt') as test_f:
    test_file = test_f.read()

ok = []
not_ok = []

test_file = {  # файл-образец.имитация открытия файла.
    'imestamp': 123,
    'referer': ' http:\\referer string (url)',
    'location': ' http:\\location string (url)',
    'remoteHost': 'remoteHost string',
    'partyId': 'partyId string',
    'sessionId': 'sessionId string',
    'pageViewId': 'pageViewId string',
    'eventType': 'itemBuyEvent или itemViewEvent',
    'item_id': 'item_id string',
    'item_price': 456,
    'item_url': ' http:\\item_url string (url)',
    'basket_price': 'basket_price string',
    'detectedDuplicate': True,
    'detectedCorruption': False,
    'firstInSession': False,
    'userAgentName': 'userAgentName string',
}

respfile = {  # файл-ответ от сервера. имтация открытия
    'imestamp': 123,
    'referer': ' http:\\referer string (url)',
    'location': ' http:\\location string (url)',
    'remoteHost': 'remoteHost string',
    'partyId': 'partyId string',
    'sessionId': 'sessionId string',
    'pageViewId': 'pageViewId string',
    'eventType': 'itemBuyEvent или itemViewEvent',
    'item_id': 'item_id string',
    'item_price': 456,
    'item_url': ' http:\\item_url string (url)',
    'basket_price': 'basket_price string',
    'detectedDuplicate': True,
    'detectedCorruption': False,
    'firstInSession': False,
    'userAgentName': 'userAgentName string',
    'secondInSession': False  # <- данная строка добавлена для проверки работы теста на количесвто строк
}

# тест сравнение количества строк файла-образца с файлом-ответом. Если оно равно то все необходимые строки есть в ответе.
if len(test_file) == len(respfile):
    print("Длинна словаря - ОК")

# тест на проверку наименования ключей (словарь) в файлай
for i in respfile:
    if i in test_file:
        ok.append(i)
    else:
        not_ok.append(i)
print('строки соответствуют требованиям: ', ok)
print('-------------')
print('строки НЕ соответствуют требованиям: ', not_ok)
print('')
print('-------------')

print('тест соответсвия объекта INT')  # тест соответсвия объекта INT
if type(respfile['imestamp']) and type(respfile['item_price']) == int:
    print("'imestamp' - OK")
    print("'item_price' - OK")
else:
    print("найдено несоответствие")
print('')
print('-------------')

print('тест соответсвия объекта str')  # тест соответсвия объекта STR
if type(respfile['remoteHost']) and type(respfile['partyId']) and type(respfile['sessionId']) and type(
        respfile['pageViewId']) and type(respfile['item_id']) and type(respfile['basket_price']) and type(
        respfile['userAgentName']) == str:
    print("'remoteHost' - OK")
    print("'partyId' - OK")
    print("'sessionId' - OK")
    print("'pageViewId' - OK")
    print("'item_id' - OK")
    print("'basket_price' - OK")
    print("'userAgentName' - OK")
else:
    print("найдено несоответствие")
print('')
print('-------------')

print('тест строки URL')  # тест налчия http:\\ или https:\\ в строке
print(test_file['referer'][0:7], '      ', respfile['referer'][0:7])
print(test_file['location'][0:7], '     ', respfile['location'][0:7])
print(test_file['item_url'][0:7], '     ', respfile['item_url'][0:7])
print('')
print('-------------')

print('тест соответсвия объекта bool')  # тест соответсвия объекта bool
if type(respfile['detectedDuplicate']) and type(respfile['detectedCorruption']) and type(
        respfile['firstInSession']) == bool:
    print("'detectedDuplicate' - OK")
    print("'detectedCorruption' - OK")
    print("'firstInSession' - OK")
else:
    print("найдено несоответствие")
