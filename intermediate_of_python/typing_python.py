from typing import Dict, List ,Set, Optional , Any, Sequence , Callable ,TypeVar
# Sequence : List, Tuple, 
age : int = 1

a : int

child : bool
if age < 18:
    child = True
else:
    child = False

s : str = "fes"
y : int = 1
z : float = 2.0
k : bool = True
b : str = "test"
f : bytes = b"test"

n : list[int] = [1,2,3,4]

x : dict[str,float] = {"num1":12}


def add_numbers(a : int | float, b : int | float, c : int | float) -> int | float:
    return  a + b + c


result = add_numbers(1,2,3)

print(result)

def print_values() -> None:
    pass

nested_list : List[List[int]] = [[1,2],[3,4]]

ayt : str = ""

vector1 = List[float]

def foo1(v : vector1) -> None:
    print(v)

def foo3(output : Optional[bool] = False) -> None:
    pass

def foo2(output : Any = False) -> None:
    pass

def foo5(output : Sequence[str]):
    pass

foo5(["1","2","3","4"])
foo5(( "a","b","c"))
# foo5({"1","2","3"}) it is not ordered

def add(x: int, y: int, z: Optional[int] = 0) -> int:
    if z is None:
        z = 0
    return x + y + z

def functionCallable(func: Callable[[int, int, Optional[int]], int], num1: int, num2: int, num3: Optional[int] = None) -> None:
    result = func(num1, num2, num3)
    print("Result:", result)

functionCallable(add, 1, 2, 0)

T = TypeVar("T")

def get_item(lst : List[T], index : int) -> T :
    return lst[index]








