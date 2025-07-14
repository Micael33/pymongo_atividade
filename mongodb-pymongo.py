from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from pprint import pprint

uri = "mongodb+srv://micaeld081:<Micael123>@cluster0.xfh9oqj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

cliente = MongoClient(uri, server_api=ServerApi('1'))

bancoDeDados = cliente['sample_mflix']

collectino_filmes = bancoDeDados['movies']

query = {"title": "The Italian"}

filme = collectino_filmes.find_one(query)

pprint(filme)

cliente.close()