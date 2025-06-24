d = list('dag iot k o p')
i, j = 0, len(d) - 1

while i < j:
    print("i", i, d[i])
    print("j", j, d[j])
    print()
    if d[i] == ' ':
        i += 1
    elif d[j] == ' ':
        j -= 1
    else:
        d[i], d[j] = d[j], d[i]
        i += 1
        j -= 1

rev_str = ''.join(d)
print(rev_str)