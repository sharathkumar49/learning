
# https://stackoverflow.com/questions/12472338/flattening-a-list-recursively

def flatten(l):
    if isinstance(l,list):
        return sum(map(flatten,l),[])
    else:
        return [l]

li=[[1,[[2]],[[[3]]]],[['4'],{5:5}]]
flatten=lambda l: sum(map(flatten,l),[]) if isinstance(l,list) else [l]  # the above function def is the expanded verison
print(flatten(li))






'''
def flatten(test_list):
    if isinstance(test_list, list):
        if len(test_list) == 0:
            return []
        first, rest = test_list[0], test_list[1:]
        return flatten(first) + flatten(rest)
    else:
        return [test_list]



'''



'''
def flatten(S):
    if S == []:
        print("coming here")
        print("S:", S)
        return S
    if isinstance(S[0], list):
        print("coming here 2nd loop")
        print("S[0]:", S[0])
        print("S[1]:", S[1:])
        return flatten(S[0]) + flatten(S[1:])
    print("coming here final")
    print("S[:1]:", S[:1])
    print("S[1:]:", S[1:])
    return S[:1] + flatten(S[1:])
'''


S = [[1,2,[3,4],5,[6,7,8],9]]
#S = [[[1,2,[3,4],5,[6,7,8],9]]]

S = [[1,2,[3,4],5,[6,[[7,8]]],9]]
print("Flattened list:",flatten(S))


