

#Source: https://medium.com/@codingpilot25/difference-between-eval-and-exec-in-python-b387b25207d2

'''
eval(): It evaluate a string which contains single expression and return the calculated value
exec(): It execute a string which contains one or more expression or statements. It always returns None.

Eval vs Exec:
Return value:
Eval function evaluates the python code and returns the value, but Exec execute the code and always returns None,
'''


#Example: We are defining simple function , which will take two arguments and returns the summation,
def add(a, b):
    return a+b

a = 'add(8,9)'
print(eval(a))
print(exec(a))
#as you can see eval() returns the summation whereas there is no output for exec because it always returns None



'''
2.Number of expression:
Eval() only evaluates the single expression, not the complex logic code, whereas Exec can be used to execute any 
number of expression.
exec() accept the source code which contains statements like, for, while, print, import, class, if we pass these 
statement to eval() it will throw error.
'''
a = 'for i in range(5):\n\tprint("hello")'
exec(a)
#and for the same input eval will produce an error


'''
3. Assignment operator:
exec can be used to assign a value to variable , but eval will throw error
'''
exec('a=5')
print(a)


'''
Conclusion:
Eval is for expression and returns the value of expression. Exec is for statement and return ‘None’
'''