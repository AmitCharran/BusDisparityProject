import pyrebase

firebaseConfig={    'apiKey': "AIzaSyAZlcTc4j8xc7Yp1ET0K0PA40rEL8MTPD4",
    'authDomain': "busgoon-f496c.firebaseapp.com",
    'databaseURL': "https://busgoon-f496c.firebaseio.com",
    'projectId': "busgoon-f496c",
    'storageBucket': "busgoon-f496c.appspot.com",
    'messagingSenderId': "534678584016",
    'appId': "1:534678584016:web:c4ffd395e1c2c21d15bcd5",
    'measurementId': "G-T0QETWNEXL"}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

def signup():
    print("Signup...")
    email=input("Enter email: ")
    password= input("Enter password: ")
    try:
        user = auth.create_user_with_email_and_password(email,password)
        print("Successfully created account")
        ask = input("Don you want to login now?[y/n]")
        if ask=='y':
            login()
    except:
        print("Email already exists!")
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