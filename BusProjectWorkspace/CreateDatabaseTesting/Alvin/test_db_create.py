# To access firebase/ the remote database
import pyrebase

# This apiKey lets us access the database for firebase
apiKey = "AIzaSyAZlcTc4j8xc7Yp1ET0K0PA40rEL8MTPD4"

# Can go to this website to see a visual representation
databaseURL = "https://busgoon-f496c.firebaseio.com"

# So far this is just copied from Firebase website after creation of a database on there
# the information is in Settings -> Project Settings. You will just need to copy paste from there
# We will need to decypher information later
firebaseConfig = {'apiKey': apiKey,
                  'authDomain': "busgoon-f496c.firebaseapp.com",
                  'databaseURL': databaseURL,
                  'projectId': "busgoon-f496c",
                  'storageBucket': "busgoon-f496c.appspot.com",
                  'messagingSenderId': "534678584016",
                  'appId': "1:534678584016:web:c4ffd395e1c2c21d15bcd5",
                  'measurementId': "G-T0QETWNEXL"}

# From pyrebase library
# initializes our database
firebase = pyrebase.initialize_app(firebaseConfig)


db = firebase.database()

#Create your own key + paths with child
data_1={"name":"Amit", "age":25, "address":["new york", "los angeles"]}
data_2={"name":"Alvin","age":30,"address":["new york","los asgard"]}
db.child("Team Member").child("Team Leader").child("Amit's info").set(data_1)
db.child("Team Member").child("Team follower").child("Alvin's info").set(data_2)