#encoding=utf-8
import requests,json

<<<<<<< HEAD
address=r'http://192.168.1.7:8080/front/register'
=======
address=r'http://192.168.1.7:8282/front/register'
>>>>>>> 9d87b533f86ccdaddcb68f8d785585def8899f4c
'''用户注册'''
def register():
    global pwd
    print("*"*40)
    print("register--------")
    data=json.dumps({'username':'ksh','password':'ksh','password2':'ksh'})
    r=requests.post(address,data=data)

    print(r.status_code)
    print(r.text)
    
register()
