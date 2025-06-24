
import os
def find_missing_ids(directory='.\LeetCodeSolutions', max_id=1247):
    missing_ids = []
    file_list = [False] * (max_id + 1)  # Initialize a list to track existing IDs
    print("file_list:", len(file_list))
    print(file_list[0], file_list[-1])
    for filename in os.listdir(directory):
        if '.py' in filename or '.sql' in filename or '.md' in filename or '.sh' in filename:
            if 'workout' in filename or 'txt' in filename:
                continue
            # print("filename:", filename)
            match_id = filename.split('.')[0]
            file_list[int(match_id)] = True

    for i, value in enumerate(file_list):
        if value == False:
            missing_ids.append(i)
    return missing_ids


# Run the function in your directory
print(find_missing_ids())
