
from timeit import timeit

code1 = '''def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less")
    return 10//age


try:
    calculate_xfactor(0)
except ValueError:
    pass'''


code2 = '''def calculate_xfactor(age):
    if age <= 0:
        return None
    return 10//age


xfactor = calculate_xfactor(0)
if xfactor == None:
    pass
'''


print("withraiseexception = ", timeit(code1, number=1000000))
print("withoutraiseexception = ", timeit(code2, number = 1000000))