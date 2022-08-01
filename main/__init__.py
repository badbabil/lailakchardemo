import pyrebase
from flask import Flask as fl

app = fl(__name__)

config = {
  "apiKey": "AIzaSyBvR1t_2k37OJ6I8zmBeYyOURdQcjl2q3w",
  "authDomain": "learnandtest-9650e.firebaseapp.com",
  "projectId": "learnandtest-9650e",
  "storageBucket": "learnandtest-9650e.appspot.com",
  "databaseURL":"https://learnandtest-9650e-default-rtdb.firebaseio.com/",
  "messagingSenderId": "771323332418",
  "appId": "1:771323332418:web:57000661e9aee054542adb",
  "measurementId": "G-SY8ENRR1Z9"
};

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

app.config['SECRET_KEY'] = 'The_Super_Secret_Key'
app.secret_key = 'The_Super_Secret_Key'

from main.templates import routes