from pymongo_get_database import get_database

dbname = get_database()
collection_name = dbname['pacientes']

paciente_1 = {
    "_id": 111,
    "nome": "Paulo Sousa",
    "telefone": "8888-8888",
    "ano_nascimento": 2000
}

paciente_2 = {
    "_id": 222,
    "nome": "Carla Dias",
    "telefone": "9999-9999",
    "ano_nascimento": 1992
}

#collection_name.insert_many([paciente_1, paciente_2])
pacientes = list(collection_name.find()) 
for paciente in pacientes:
    print(paciente)

