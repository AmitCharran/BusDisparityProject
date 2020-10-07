import urllib

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

#setting up storage
storage= firebase.storage()

#upload a file to storage
file=input("Enter the name of the file you want to upload to storage:")
cloudfilename=input("Enter the name for the file in storage")
storage.child(cloudfilename).put(file)

#get url
print(storage.child(cloudfilename).get_url(None))

#download
downloadlink=input("Enter download url")
storage.child(downloadlink).download("downloaded.txt")

#read from a file
path=input("Enter the path in storage of the file you want to read")
print(storage.child(path).get_url(None))
url=storage.child(path).get_url(None)
f=urllib.request.urlopen(url).read()
print(f)