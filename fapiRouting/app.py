from fastapi import FastAPI
app=FastAPI()

'''
Usage:Application Root
Rest API URL: http://127.0.0.1:8000/
Method Type: GET
Required Feilds: None
Access Type: Public
'''

@app.get("/")
def root_request():
    return "Application Root Request"