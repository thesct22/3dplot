from firebase import firebase
from requests import get
firebase= firebase.FirebaseApplication('https://air-conditioning-12b11.firebaseio.com/')
ip = get('https://api.ipify.org').text
result1 = firebase.put('https://air-conditioning-app.firebaseio.com/','ip',ip)
