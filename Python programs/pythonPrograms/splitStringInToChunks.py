

def split_into_chunks(string, chunk_size):
    return [string[i:i+chunk_size] for i in range(0, len(string), chunk_size)]

# Example usage
long_string = "ThisIsALongStringThatNeedsSplitting"
chunk_size = 4
chunks = split_into_chunks(long_string, chunk_size)
print(chunks)



# In this code:
#
# The split_into_chunks function takes a string and a chunk_size as input.
#
# It uses a list comprehension to create a list of substrings, each of the specified chunk_size.
#
# The range(0, len(string), chunk_size) generates indices at intervals of chunk_size.
#
# The substring is taken from each index up to chunk_size.