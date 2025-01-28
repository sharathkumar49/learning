
import sys

for line in sys.stdin:
    if 'bruce' == line.strip():
        break
    print(f'Input: {line}')
print('exit')

#sys.stdout
sys.stdout.write("Bruce wayne\n")



