
import time

start_time = time.time()
large_list = [x*x for x in range(10000000)]
for i in large_list:
    pass
print("time taken :", time.time() - start_time)


start_time = time.time()
gen_list = (x*x for x in range(10000000))
for i in gen_list:
    pass
print("time taken :", time.time() - start_time)


print([lambda x: x*x for _ in range(3)])