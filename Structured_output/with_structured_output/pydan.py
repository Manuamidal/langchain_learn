from pydantic import BaseModel,EmailStr,Field
from typing import Optional

class Person(BaseModel):
    name:str
    age:Optional[int]=None
    email:EmailStr
    cgpa:float=Field(gt=0.0,lt=4.0,default=3.0,description="CGPA must be between 0.0 and 4.0")
    
student={"name":"Alice","age":20,"email":"alice@example.com","cgpa":3.8}

person=Person(**student)

per_dict=dict(person)

print(per_dict["email"])

  # Output: alice@example.com
print(person.model_dump_json())