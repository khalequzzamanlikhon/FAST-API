
from fastapi import FastAPI, Path, HTTPException
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

######################################################################### Basic #####################################################
@app.get("/")
def home():
    return "FAST API IS fascinating"


''' 

there are two types of end point parameters : path and query param. the main differences is that for path
variable we need to write the parameter name both in the endpoint url but for query parameter we just need to 
write in the function

'''
students = {
    0: {"name": "John", "age": 17, "grade": "A"},
    1: {"name": "Jane", "age": 18, "grade": "B"},
    2: {"name": "Doe", "age": 19, "grade": "C"}
}


# ######################################################### path parameter ################################################################
@app.get("/get-student/{student_id}")
def get_student(student_id: Optional[int] = Path(..., description="Enter the ID of the student", ge=0, le=2)):
    if student_id not in students:
        raise HTTPException(status_code=404, detail="Student not found")
    return students[student_id]

#########################################################   query parameter ##################################################################

''' 
   multiple query param: we can add multiple but there are guidelines.
     non-default argument can't follow default argument. to avoid error we can use.
    In other words it doesn't support optional argument before required argument.


'''
@app.get("/get-by-sname")
def get_student_byname(*, name: Optional[str] = None, id: int):
    if id in students:
        if students[id]["name"] == name:
            return students[id]
        else:
            return students[id]
    return "Value is not in the list"

############################################################### query and path   ##############################################################


@app.get("/get-age/{student_age}")
def get_student_age(*,student_id: int, age: int ):
    if student_id in students:
        if students[student_id]["age"]== age:
            return age
        else:
            return "the id holder's age doesn't match with the given age"
    return " There is no entry regarding this input"




############################################## Request body and the post method ########################################################

# Example for creating a student (POST request)
class Student(BaseModel):
    name: str
    age: int
    grade: str


@app.post("/create-student/{student_id}")
def create_student(student_id: int, student: Student):
    if student_id in students:
        raise HTTPException(status_code=400, detail="Student ID already exists")
    students[student_id] = student
    return students[student_id]

