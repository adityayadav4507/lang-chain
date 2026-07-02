from typing import TypedDict

## we define the structure of the dict
class Person(TypedDict):
    name: str
    age: int

person_1 : Person={'name':'aditya',
                   'age':23}
print(person_1)

## no. validation -> means you can make str also no error through
## it just suggest that you have to use the int

person_2 : Person={'name':'aditya',
                   'age':'23'}
print(person_2)