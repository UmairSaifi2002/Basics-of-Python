# Type hints in Python help provide clarity about the types of variables, function parameters, and return values. 
# While Python doesn’t enforce types at runtime, 
# type hints improve code readability and help tools like linters, IDEs, and type checkers (e.g., mypy) to catch errors early.

age : int = 21
name : str = "umair"
price : float = 999.99
is_Active : bool = True

# Function Type Hints
# Parameter Hints: Specify the types of input arguments.
# Return Type Hint: Use -> to specify the return type.   

def greetig(name : str) -> str:
    return f"Hello,\nGood Morning {name}!"  
print(greetig("Umair"))          
print(type(greetig("Umair")))

# ---------- X ---------- X ----------
num1 : int = 1
num2 : int = 2

def Sum(num1 : int, num2 : int) -> int:
    return num1+num2

a = Sum(num1,num2)
print(a)
print(type(a))

# ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ----------

from typing import Tuple, Dict, List, Set, Union

def sum_of_numbers(numbers : List[int]) -> int:
    return sum(numbers)

print(sum_of_numbers([1, 2, 3, 4]))

# ---------- X ---------- X ----------

def get_person_details() -> Tuple[str, int]:
    return "Alice", 30

print(get_person_details())

# ---------- X ---------- X ----------

def count_frequencies(words: List[str]) -> Dict[str, int]:
    return {word: words.count(word) for word in set(words)}

print(count_frequencies(["apple", "banana", "apple"]))

# ---------- X ---------- X ----------

def process_data(data: Union[int, str]) -> str:
    if isinstance(data, int):
        return f"Processed number: {data}"
    elif isinstance(data, str):
        return f"Processed string: {data}"

print(process_data(42))       # Output: Processed number: 42
print(process_data("hello"))  # Output: Processed string: hello
