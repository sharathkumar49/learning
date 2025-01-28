num = int(input("Enter the prime factors of a given number: "))
for i in range(2, num):
    if num%i==0:
        print(i)

        #wrong do it again#
        #search for prime factors of a given number