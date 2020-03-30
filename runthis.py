from firebase import firebase
from requests import get
<<<<<<< HEAD
firebase= firebase.FirebaseApplication('https://air-conditioning-12b11.firebaseio.com/')
ip = get('https://api.ipify.org').text
result1 = firebase.put('https://air-conditioning-app.firebaseio.com/','ip',ip)
=======
ip = get('https://api.ipify.org').text
result1 = firebase.put('https://air-conditioning-app.firebaseio.com/','ip',ip)
>>>>>>> 022a22a43368e6d5e0e3255a66704c0a9649f6c0
