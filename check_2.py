from firebase import firebase

firebase = firebase.FirebaseApplication('https://striped-harbor-275119.firebaseio.com/', None)


data =  { 'Name': 'Vivek',
          'RollNo': 1,
          'Percentage': 76.02
          }

result = firebase.put('','/Potholeinfo/path4',data)

print(result)