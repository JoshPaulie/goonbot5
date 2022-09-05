from keys import MONGO_PW
from motor.motor_asyncio import AsyncIOMotorClient as MotorMongoClient

mongo_url = f"mongodb+srv://bexli:{MONGO_PW}@goonbot-cluster.olodjti.mongodb.net/?retryWrites=true&w=majority"
client = MotorMongoClient(mongo_url)
db = client["db"]
