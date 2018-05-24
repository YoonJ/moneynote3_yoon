import pyrebase

# pyrebase setting
config = {
    "apiKey": "AIzaSyANgDGfzUIprlmVjTvY383c_-etqd8ZHIc",
    "authDomain": "kcuo-e6a26.firebaseapp.com",
    "databaseURL": "https://kcuo-e6a26.firebaseio.com",
    "projectId": "kcuo-e6a26",
    "storageBucket": "kcuo-e6a26.appspot.com",
    "messagingSenderId": "644548812510"
}
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()

email="oyoons95@gmail.com"
password="20180101"

user = auth.sign_in_with_email_and_password(email, password)

#
data = {
    "name": "김채우오",
    "email": "1234@gmail.com",
}


def insert_data():
    #db.child("users").push(data)
    #with key
    db.child("users").child("test").set(data)


def update(string_key, string_data):
    db.child("users").child(string_key).update(string_data)

def remove(string_key):
    db.child("users").child(string_key).remove()

def get_data(string1):
    datatmp = db.child("users").child(string1).get()
    print(datatmp.val())

insert_data()
