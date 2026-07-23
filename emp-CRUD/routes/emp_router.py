from fastapi import APIRouter
from models.emp import Employee
from pymongo import MongoClient

#create employee router
router=APIRouter(prefix='/emp')

#establish the db connection
client=MongoClient('mongodb://localhost:27017')
db=client['dbtwo']
emp_col=db['employees']



'''
usage:Create new Employee
Rest API URL: http://127.0.0.1:8000/emp/create
Method Type:POST
Request Fields:eid,ename,esal,gender 
Access Type:Public
'''
@router.post("/create")
def create_emp(emp:Employee):
    emp_col.insert_one(emp.dict())
    return {'msg':'New Employee Created succesfully'}