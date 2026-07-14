from fastapi import FastAPI

app=FastAPI()

'''
Usage: Application Root Request
Rest API URL: http://127.0.0.1:8000/
Method Type:GET
Required Fields: None 
Acccess Type:Public
'''
@app.get("/")
def index_page():
    return {"msg":"Index Page"} 


'''
Usage: About Page
Rest API URL: http://127.0.0.1:8000/about
Method Type:GET
Required Fields: None 
Acccess Type:Public
'''
@app.get("/about")
def about_page():
    return {"msg":"About Page"}  

'''
Usage: Contact Page
Rest API URL: http://127.0.0.1:8000/contact
Method Type:GET
Required Fields: None 
Acccess Type:Public
'''
@app.get("/contact")
def contact_page():
    return {"msg":"Contact Page"} 


'''
Usage: Login Page
Rest API URL: http://127.0.0.1:8000/login
Method Type:GET
Required Fields: None 
Acccess Type:Public
'''
@app.get("/login")
def login():
    return {"msg":"Login Page"} 


'''
What is Virtual Env?
How to active VENV?

Install packages

How to start server?
uvicorn server:app --reload

'''