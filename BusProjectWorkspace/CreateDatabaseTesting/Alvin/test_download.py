import urllib
import urllib.request
# This is our database
import pyrebase

# So far this is just copied from Firebase website after creation of a database on there
# the information is in Settings -> Project Settings. You will just need to copy paste from there
# We will need to decypher information later
firebaseConfig={'apiKey': "AIzaSyAZlcTc4j8xc7Yp1ET0K0PA40rEL8MTPD4",
    'authDomain': "busgoon-f496c.firebaseapp.com",
    'databaseURL': "https://busgoon-f496c.firebaseio.com",
    'projectId': "busgoon-f496c",
    'storageBucket': "busgoon-f496c.appspot.com",
    'messagingSenderId': "534678584016",
    'appId': "1:534678584016:web:c4ffd395e1c2c21d15bcd5",
    'measurementId': "G-T0QETWNEXL"}

# From pyrebase library
# initializes our database
# Note this is not a new database - this is from online from the firebase website
firebase = pyrebase.initialize_app(firebaseConfig)

storage = firebase.storage()

<<<<<<< HEAD
path = "book/info.txt"
url = storage.child(path).get_url(None)
storage.child(url).download("downloadedHowdy3.txt")
print(storage.child(path).get_url(None))
f = urllib.request.urlopen(url).read()
=======
path = "Oct11.txt"
>>>>>>> 99f1a80ad432130ca28dbbcccac17586d44f6996

storage.child(path).download("downloadedHowdy3.txt")

