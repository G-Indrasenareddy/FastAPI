from fastapi import FastAPI
app=FastAPI()

users=[
    {"uid":101,"uname":"RG","Avail":True,"discount":None},
    {"uid":102,"uname":"SG","Avail":False},
    {"uid":103,"uname":"PG","Avail":True},
    {"uid":104,"uname":"NM","Avail":True},
]

'''
usage:Application Root Request
Rest API URL: http://127.0.0.1:8000/
Method Type:GET
Required Fields:None
Access Type:public
'''
@app.get("/")
def root_req():
    return {"msg":"Appliation Root Request"}


'''
usage:Application Root Request
Rest API URL: http://127.0.0.1:8000/users/read
Method Type:GET
Required Fields:None
Access Type:public
'''
@app.get("/users/read")
def fetch_users():
    return users