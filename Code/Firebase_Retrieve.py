import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Connect to Firebase
cred = credentials.Certificate('../FirebaseKey/fingergesturerecognitionsystem-firebase-adminsdk-xcpqf-cf83d06251.json')  # get service account key JSON
# initialize with service account to get admin privileges
default_app = firebase_admin.initialize_app(cred, {
    #'databaseURL': databaseURL
    'databaseURL': "https://fingergesturerecognitionsystem-default-rtdb.firebaseio.com/"

})

# retrieve data
ref = db.reference('/')
data = ref.get()
print(data)
