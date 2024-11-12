from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os

load_dotenv()

uri = os.getenv("DATABASE_URL")

# Create a new client and connect to the server
client = MongoClient(
    uri,
    tls=True,  # Explicitly enable TLS/SSL
    tlsAllowInvalidCertificates=False,  # Ensure the certificate is valid
    server_api=ServerApi('1')
    )

db = client.todo_db
collection = db["tasks_data"]