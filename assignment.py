def main():
    # Array with exactly 5 elements where a pair sums to 9
    x = [3, 6, 5, 2, 4]  

    print("Original Array:", x)

    # Efficient search using HashSet (O(n))
    def find_pair_with_sum(arr, target_sum):
        seen = set()  # HashSet 4 storing elements
        for num in arr:
            complement = target_sum - num  # Find the required num
            if complement in seen:
                return f"Pair found: {num} + {complement} = {target_sum}"
            seen.add(num)  # Store the number in HashSet
        return "No pair found"

    print(find_pair_with_sum(x, 9))

if __name__ == "__main__":
    main()
