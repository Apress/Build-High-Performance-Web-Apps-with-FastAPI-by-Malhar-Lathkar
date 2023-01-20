arg1: int = int(input("Enter a number.."))
arg2: int = int(input("Enter a number.."))

def division(num:int, den:int) -> float:
    result:float = num/den
    return result

print (division(arg1, arg2))   
