from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import BaseModel,EmailStr,Field
from dotenv import load_dotenv
from typing import Optional

load_dotenv()

class student(BaseModel):
    name:str
    last_name:str ='yadav' ### for default value
    age:Optional[int]=None  ## for optional when nothing then give None
    roll:Optional[int]
    email:EmailStr  ## email validator 
    cgpa:float =Field(gt=0,lt=10,description="value is float") ## apply constraints

student1={'name':'aditya','age':23,
          'roll':'11','email':'abd@gamil.com','cgpa':2
          } ## pydantic convert roll into int

s=student(**student1)

print("class =",s)
print()
print("dic = ",dict(s))
print()
print("json = ",s.model_dump_json())


