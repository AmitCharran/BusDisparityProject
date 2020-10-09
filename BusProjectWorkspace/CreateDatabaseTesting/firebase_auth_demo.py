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

# this object lets will authorize us to work with firebase
auth = firebase.auth()


# These functions are useless for now
# But I still like that they are included - Amit
# These are functions so we can sign-up
def signup():
    print("Signup...")
    email = input("Enter email: ")
    password = input("Enter password: ")
    try:
        user = auth.create_user_with_email_and_password(email, password)
        print("Successfully created account")
        ask = input("Don you want to login now?[y/n]")
        if ask == 'y':
            login()
    except:
        print("Email already exists!")

# this function is to log in with the future
def login():
    print("Log in...")
    email = input("Enter email:")
    password = input("Enter password:")
    try:
        login=auth.sign_in_with_email_and_password(email,password)
        print("Successfully logged in!")
        print(auth.get_account_info(login['idToken']))
    except:
        print("Email already exists!")

ans=input("Are you a new user?[y/n]")
if ans=='y':
    signup()
elif ans=='n':
    login()