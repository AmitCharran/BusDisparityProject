


# for handling URLs
import urllib
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





########################################################################################
# Testing upload
# setting up storage
storage = firebase.storage()

# This prompts the user for file name -- which is 'test_upload.txt'
file = input("Enter the name of the file you want to upload to storage: ")


# This is how to define the file path and name in the firebase storage
cloud_file_name = input("Enter the name for the file in storage: ")

# This is line of code is how you actually upload the file
storage.child(cloud_file_name).put(file)

# This is the link to the website to get the information
print(storage.child(cloud_file_name).get_url(None))







########################################################################################
# Testing grabbing information from database
# setting up storage
storage = firebase.storage()
# Prompts the user for information
download_link = input("Enter download file: ")
storage.child(download_link).download("downloadedHowdy2.txt")

# setting up storage
storage = firebase.storage()
# read from a file
# prompts the user for file path
path = input("Enter the path in storage of the file you want to read: ")

# this is the link to the storage to grab the information
print(storage.child(path).get_url(None))


# This part needs work
# request to grab information
url = storage.child(path).get_url(None)
f = urllib.request.urlopen(url).read()

# with open("test_download.txt" , "w") as file:
#     data = file.load(f)
print(f)
