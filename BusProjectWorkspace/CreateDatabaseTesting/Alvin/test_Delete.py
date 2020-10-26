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

# #Delete item with known key
# db.child("todolistA").child("wednesday").child("volunteer").child("deadline").remove()
#
# #Delete entire node and its children
# db.child("todolistA").child("tuesday").remove()
#
# #Delete item with unkown generated key
# monday_tasks=db.child("todolistB").child("monday").get()
#
# for task in monday_tasks.each():
#     if task.val()['name']=="paper":
#         key=task.key()
#
# db.child("todolistB").child("monday").child(key).child("deadline").remove()

tasks = db.child("MTA").get()


print(tasks)
# db.child("MTA").remove()

