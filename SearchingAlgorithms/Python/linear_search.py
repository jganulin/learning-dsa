import random


# Searches 'arr' for 'target' using linear search, returning its index if found, -1 if not
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


# Driver to test the function
if __name__ == "__main__":
    arr = random.sample(range(10), 10)
    el = random.choice(arr)
    print("List:", arr)
    print("Searching for", el)
    print(el, "found at index", linear_search(arr, el))

