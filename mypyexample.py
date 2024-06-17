from typing import List, Dict

def add_numbers(a, b):
    return a + b

def get_number() -> int:
    return "42"

def get_list_of_strings() -> List[str]:
    return [1, 2, 3]

def get_person_info() -> Dict[str, int]:
    return {"name": "Alice", "age": "30"}

def greet(name: str) -> None:
    print(f"Hello, {name}!")

greet(123)  

x: str = 42

def multiply(a, b):
    return a * b

def use_uninitialized_variable():
    if some_condition:
        value = 10
    print(value)

some_condition = False
