def generate_partitions(n, max_num=None, current_partition=None):
    print("n, max_num, current_partition: ", n, max_num, current_partition)
    if current_partition is None:
        current_partition = []
        print("current_partition inside None: ", current_partition)
    print("current_partition: ", current_partition)

    if max_num is None:
        max_num = n
        print("max_num: ", max_num)

    if n == 0:
        print("curren_partition when n = 0", current_partition)  # Print partition when n reaches 0
        return

    for i in range(min(n, max_num), 0, -1):  # Iterate in decreasing order
        print("\n\nIterating in decreasing order: i, ", i)
        generate_partitions(n - i, i, current_partition + [i])

# Example usage:
# num = int(input("Enter a number to partition: "))
num = 4
generate_partitions(num)
