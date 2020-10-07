#Note - This is still a work in progress

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
cloud_file_name = input("Enter the name for the file in storage: ")

# This is line of code is how you actually upload the file
storage.child(cloud_file_name).put(file)

# This is the link to the website to get the information
print(storage.child(cloud_file_name).get_url(None))







########################################################################################
# Testing grabbing information from database

# Prompts the user for information
download_link=input("Enter download url: ")
storage.child(download_link).download("downloaded.txt")

# read from a file
# prompts the user for file path
path = input("Enter the path in storage of the file you want to read: ")

# this is the link to the storage to grab the information
print(storage.child(path).get_url(None))


# This part needs work
# request to grab information
url = storage.child(path).get_url(None)
f = urllib.request.urlopen(url).read()
print(f)