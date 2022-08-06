import random


# Searches 'arr' for 'target' using binary search, returning its index if found, -1 if not
# Requires a sorted array/list. O(log2(n)) Time
def binary_search(arr, target):



# Driver to test the function
if __name__ == "__main__":
    arr = random.sample(range(10), 10)
    el = random.choice(arr)
    print("List:", arr)
    print("Searching for", el)
    print(el, "found at index", binary_search(arr, el))
