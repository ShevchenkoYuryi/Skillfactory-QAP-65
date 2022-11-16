# Created user object
сreate_user = {
  "id": 0,
  "username": "Hanter",
  "firstName": "Jon",
  "lastName": "Rambo",
  "email": "jrambo@mail.ru",
  "password": "allb",
  "phone": "+79998887766",
  "userStatus": 0
}

# updated user
update_user ={
  "id": 0,
  "username": "Driver",
  "firstName": "Mike",
  "lastName": "Shumaher",
  "email": "mshumaher@mail.ru",
  "password": "alla",
  "phone": "322589",
  "userStatus": 0
}

# Add a new pet to the store
body = {
  "id": 0,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "doggie",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}

# order
body_order = {
  "id": 0,
  "petId": 0,
  "quantity": 0,
  "shipDate": "00/00/0000",
  "status": "placed",
  "complete": True
}