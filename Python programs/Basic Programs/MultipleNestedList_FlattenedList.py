

def flatten(S):
    if S == []:
        return S
    if isinstance(S[0], list):
        return flatten(S[0]) + flatten(S[1:])
    return S[:1] + flatten(S[1:])


S = [[1,2,[3,4],5,[6,7,8],9]]


print("flattend list:", flatten(S))


"""
1. It will go to the 2nd if loop 'if isinstane(S[0], list)' 
   since, we don't have S[1:] and only have S[0] at this point
   which means, S[0] = [1,2,[3,4],5,[6,7,8],9]
                S[1] = nothing
"""


