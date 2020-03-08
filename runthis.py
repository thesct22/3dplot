from requests import get
ip = get('https://api.ipify.org').text
result1 = firebase.put('https://air-conditioning-12b11.firebaseio.com/','ip',ip)