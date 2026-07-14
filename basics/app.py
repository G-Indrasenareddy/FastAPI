# from fastapi import FastAPI
# app = FastAPI()

# @app.get("/")
# def wish():
#     return {"msg":"Good Evening"}


# from fastapi import FastAPI
# app=FastAPI()

# '''
# Usage: Application Root Request
# Rest API URL: http://127.0.0.1:8000/
# Method Type:GET
# Requried Fields:None
# Access Type:public
# '''
# @app.get("/")
# def root_request():
#     return {'msg':True}


from fastapi import FastAPI
app=FastAPI()

'''
Usage: Application Root Request
Rest API URL: http://127.0.0.1:8000/
Method Type:GET
Requried Fields:None
Access Type:public
'''
@app.get("/")
def root_request():
    return {'msg':True}


'''
Usage: create new User
Rest API URL: http://127.0.0.1:8000/create
Method Type:POST
Requried Fields:uid,uname,age
Access Type:public
'''
@app.post("/create")
def create_new_User():
    return {"msg":"New User created successfully"}

'''
Usage: fetch all users
Rest API URL: http://127.0.0.1:8000/read
Method Type:GET
Requried Fields:None
Access Type:public
'''

@app.get("/read")
def get_users():
    return {"msg":"Featching all user details"}

'''
Usage: update user by id
Rest API URL: http://127.0.0.1:8000/update
Method Type:PUT
Requried Fields:None
Access Type:public
'''
@app.put("/update")
def update_user():
    return {'msg':"User Updated successfully"}


'''
Usage: Delete user by id
Rest API URL: http://127.0.0.1:8000/delete
Method Type:DELETE
Requried Fields:None
Access Type:public
'''

@app.delete("/delete")
def delete_user():
    return {"msg":"User Deleted successfully"}