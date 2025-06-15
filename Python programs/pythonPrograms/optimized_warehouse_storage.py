
# Optimized Warehouse Storage
# A warehouse has shelves of different heights. 
# Given a list of box heights, determine the minimum number of shelves
# needed such that no shelf exceeds a fixed height limit. 

# Input: boxes = [8, 5, 12, 6, 15, 7], shelf_height_limit = 20
# Output: 3 (shelves used: [8, 5, 6], [12, 7], [15])



def min_shelves(boxes, shelf_height_limit):
    boxes.sort(reverse=True)  # Sort boxes in descending order
    shelves = []  # List to hold the current shelves

    for box in boxes:
        placed = False
        for i in range(len(shelves)):
            if sum(shelves[i]) + box <= shelf_height_limit:
                shelves[i].append(box)
                placed = True
                break
        if not placed:
            shelves.append([box])  # Create a new shelf for this box

    return len(shelves)


# Example usage 
if __name__ == "__main__":
    boxes = [8, 5, 12, 6, 15, 7]
    shelf_height_limit = 20
    print("Minimum shelves used:", min_shelves(boxes, shelf_height_limit))  # Output: 3







def min_shelves(boxes, shelf_height_limit):
    boxes.sort(reverse=True)  # Sort largest to smallest
    left, right = 0, len(boxes) - 1
    shelves = 0

    while left <= right:
        if boxes[left] + boxes[right] <= shelf_height_limit:
            right -= 1  # Pair the smallest available box with the largest
        left += 1
        shelves += 1

    return shelves

# Example usage
boxes = [8, 5, 12, 6, 15, 7]
shelf_height_limit = 20
print("Minimum number of shelves:", min_shelves(boxes, shelf_height_limit))  # Output: 3



