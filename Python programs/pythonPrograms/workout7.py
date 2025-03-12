# nums = [1, 2, 3]
#
# print(dir(nums))
#
# i_nums= nums.__iter__()
#
# print(i_nums)
#
# print(dir(i_nums))
#
# print(i_nums.__iter__())
#
# print(i_nums.__next__())
# print(i_nums.__next__())
# print(i_nums.__next__())
# print(i_nums.__next__())
#

# for i in nums:

lst_comprehension = (x*x for x in [1, 2, 3, 4, 5])

print(lst_comprehension)


print(lst_comprehension.__next__() )
