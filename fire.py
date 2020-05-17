import pyrebase


firebaseConfig = {
    "apiKey": "AIzaSyA_z6AItTzLoNySATe_2VaSmnBYMLM0Zx8",
    "authDomain": "leave-management-9cf8f.firebaseapp.com",
    "databaseURL": "https://leave-management-9cf8f.firebaseio.com",
    "projectId": "leave-management-9cf8f",
    "storageBucket": "leave-management-9cf8f.appspot.com",
    "messagingSenderId": "363355666002",
    "appId": "1:363355666002:web:c59a452d161e42714c518b",
    "measurementId": "G-G090FRGWMJ"
    }

firebase = pyrebase.initialize_app(firebaseConfig)

auth=firebase.auth()
db = firebase.database()
