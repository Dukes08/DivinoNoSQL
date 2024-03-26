from pymongo import MongoClient
import certifi

MONGO_URI = 'mongodb+srv://hugoduque:cucaracha2Ah@cluster.jnqlvks.mongodb.net/?retryWrites=true&w=majority&appName=Cluster'
ca = certifi.where()

def dbConnection():
    try:
        client = MongoClient(MONGO_URI, tlsCAFile=ca)
        db = client["dbb_products_app"]
    except ConnectionError:
        print('Error de conexión con la bdd')
    return db
