# Created user object

create_user = {
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

#List of user object

list_u = [
  {
  "id": 0,
  "username": "capitan",
  "firstName": "Jack",
  "lastName": "Sparow",
  "email": "jack@mail.ru",
  "password": "all4",
  "phone": "none",
  "userStatus": 0
  },
  {
  "id": 0,
  "username": "Master",
  "firstName": "Leonardo",
  "lastName": "DaVinchi",
  "email": "leo@mail.ru",
  "password": "all5",
  "phone": "none",
  "userStatus": 0
  }
]


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
  "shipDate": "0",
  "status": "placed",
  "complete": True
}