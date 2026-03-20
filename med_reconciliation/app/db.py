from pymongo import MongoClient
client = MongoClient("your_mongodb_connection_string"
)
db = client.med_db

patients_col = db.patients
snapshots_col = db.snapshots
conflicts_col = db.conflicts