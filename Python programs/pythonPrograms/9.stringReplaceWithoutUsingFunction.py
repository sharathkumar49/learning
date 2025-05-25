

def replace_custom(target: str, to_be_replaced: str, replace_with: str) -> str:
    print("length of target: ", len(target))
    print("length of tobe replaced: ", len(to_be_replaced))
    print("length difference: ",len(target)-len(to_be_replaced)+1 )
    for i in range(len(target)-len(to_be_replaced)+1):
        print("inside for loop:", i)
        print(i,len(to_be_replaced) + i)
        if target[i:len(to_be_replaced) + i] == to_be_replaced:
            new_target = '{}{}{}'.format(target[:i], replace_with, target[i + len(to_be_replaced):])
            return replace_custom(new_target, to_be_replaced, replace_with)
    return target


a = 'andappleapple'
b = 'apple'
c = 'banana'
print(replace_custom(a, b, c))