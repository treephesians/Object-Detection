# Function that I need.

def remove_extension(arr):
    for _ in range(len(arr)):
        arr[_] = arr[_].split('.')[0]
    return arr