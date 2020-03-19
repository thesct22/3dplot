from firebase import firebase
from requests import get
ip = get('https://api.ipify.org').text
result1 = firebase.put('https://air-conditioning-app.firebaseio.com/','ip',ip)