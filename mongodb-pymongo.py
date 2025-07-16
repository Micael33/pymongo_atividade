from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from pprint import pprint

uri = "mongodb+srv://micaeld081:Micael123@cluster0.xfh9oqj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(uri, server_api=ServerApi('1'))

bancoDeDados = client['sample_mflix']

collectino_filmes = bancoDeDados['movies']

query = {"title": "The Italian"}

try:

    filme = collectino_filmes.find_one(query)
    if filme:
        print("filme encontrado")
        pprint(filme)
    else:
        print("filme nao encontrado")

except Exception as e:
    print(f'Ocorreu um erro: {e}')

finally:
    client.close()
    