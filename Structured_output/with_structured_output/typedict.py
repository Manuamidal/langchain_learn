from typing import TypedDict

class Person(TypedDict):
     name: str
     age: int

student : Person = {"name": "Alice", "age": 20}

print(student)  # Output: {'name': 'Alice', 'age': 20}