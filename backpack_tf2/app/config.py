from dotenv import load_dotenv
import os

load_dotenv()

BACKPACK_API_KEY = os.getenv("BACKPACK_API_KEY")
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
MONGODB_IP = os.getenv("MONGO_DOCKER_IP_ADDRESS")
MONGODB_PORT = int(os.getenv("MONGO_DOCKER_PORT", default=27017))
MONGO_DB_NAME = os.getenv("MONGO_DB_NAME", default="backpackdb")
