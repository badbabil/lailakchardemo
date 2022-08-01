import pyrebase

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

# db = firebase.database()

email = 'zynos007@gmail.com'
password = '123456'

user = auth.sign_in_with_email_and_password(email,password)
user = auth.get_account_info(user['idToken'])
print(user)
# if user['User'][0]['emailVerified']==False:
#   print(f'Email not verified, Please verify (check for verification mail) and login','danger')
# try:
#   user = auth.create_user_with_email_and_password(email,password)
# except:
  # print(type(Exception))
# auth.send_email_verification(user['idToken'])


# print(user)