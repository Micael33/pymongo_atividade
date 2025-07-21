import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.server_api import ServerApi
from pprint import pprint

uri = "mongodb+srv://micaeld081:Micael123@cluster0.xfh9oqj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

async def find_filme():
    client = AsyncIOMotorClient(uri, server_api=ServerApi('1'))
    try:
        database = client['sample_mflix']
        coll_filme = database['movies']

        query = {"title": "Regeneration"}

        filme = await coll_filme.find_one(query)
        if filme:
            print("filme encontrado")
            pprint(filme)
        else:
            print("filme nao encontrado")
    
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
    
    finally:
        await client.close()
    
asyncio.run(find_filme())
   