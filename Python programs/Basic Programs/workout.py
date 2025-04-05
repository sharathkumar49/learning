
source = {1:'a', 2:'b', 3:'c',4:'a', 5:'a', 6:'d', 7: 'e', 8:'b', 9:'c'}
#output = {'a': [1,4,5], 'b': [2,8], 'c': [3,9], 'd': [6], 'e': [7]}

output = {}

for k,v in source.items():
   if v in output:
     output[v].append(k)
   else:
    output.update({v :[k]})


print(output)
