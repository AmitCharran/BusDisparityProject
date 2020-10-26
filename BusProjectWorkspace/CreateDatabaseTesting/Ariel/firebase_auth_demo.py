# how to access firebase
import pyrebase

# this is the configuration of the firebase
firebaseConfig = {"apiKey": "AIzaSyAZlcTc4j8xc7Yp1ET0K0PA40rEL8MTPD4",
                  "authDomain": "busgoon-f496c.firebaseapp.com",
                  "databaseURL": "https://busgoon-f496c.firebaseio.com",
                  "projectId": "busgoon-f496c",
                  "storageBucket": "busgoon-f496c.appspot.com",
                  "messagingSenderId": "534678584016",
                  "appId": "1:534678584016:web:c4ffd395e1c2c21d15bcd5",
                  "measurementId": "G-T0QETWNEXL"}

# this is the initialization of our database as well as authorize the use of it
firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()


# this is for logging into the database, as well as creating an account for the database
# good for practice

def signup():
    print("Sign up...")
    email = input("Enter email:")
    password = input("Enter password:")
    try:
        user = auth.create_user_with_email_and_password(email, password)
        print("successfully created account")
        ask = input("Do you want to login in now?[y/n]")
        if ask == 'y':
            login()
    except:
        print("Email already exists")


def login():
    print("Log in...")
    email = input("Enter email:")
    password = input("Enter password:")
    try:
        login = auth.sign_in_with_email_and_password(email, password)
        print("Succesfully logged in!")
    except:
        print("Invalid password!")


ans = input("Are you a new user? [y/n]")
if ans == 'y':
    signup()
elif ans == 'n':
    login()
