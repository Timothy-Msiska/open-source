import bisect

def main():
    # Initial array
    x = [3, 1, 5, 2, 4]

    # Sort the array (O(n log n))
    x.sort()
    print("Sorted Array:", x)

    # Efficient search using Binary Search (O(log n))
    def search(arr, target):
        index = bisect.bisect_left(arr, target)
        if index < len(arr) and arr[index] == target:
            return f"Element {target} found at index {index}"
        else:
            return f"Element {target} not found"

    print(search(x, 5))  # Search for 5

    # Insert element efficiently while maintaining order (O(n))
    bisect.insort(x, 6)
    print("Array after inserting 6:", x)

if __name__ == "__main__":
    main()
