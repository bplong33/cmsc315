"""
=====================================================
UNIT 5 DISCUSSION: SEARCH ALGORITHMS (LINEAR vs BINARY)
=====================================================

INSTRUCTIONS:
In this assignment, you will implement and analyze two
fundamental search algorithms: linear search and binary search.

You will demonstrate your understanding by modifying the
provided code, running experiments on different dataset sizes,
and clearly explaining your results through code comments
and program output.
"""

from typing import Any
import time
import random


def linear_search(lst: list[Any], target: Any) -> int:
    """
    TODO (Student):
    Implement a linear search algorithm.

    Requirements:
    - Search the list from beginning to end.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining why linear search
      has O(n) time complexity.
    """

    # we need to check every index linearly to test if it equals the searched value
    # We could search starting from the end or from the beginning, but either
    # way, the worst case scenario would mean checking every index
    for i in range(len(lst)):
        if lst[i] == target:
            return i

    # if we make it through the for loop and don't find the value and return the index,
    # then the value didn't exist, so return -1
    return -1


def binary_search(lst: list[Any], target: Any) -> int:
    """
    TODO (Student):
    Implement a binary search algorithm.

    Requirements:
    - Assume the list is already sorted.
    - Repeatedly reduce the search space by half.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining how each iteration
      reduces the search space.
    """
    # assuming low boundary is 0 and high is the last index to start, set the low and high
    low = 0
    high = len(lst) - 1

    while low <= high:
        # determine the midpoint based on the current high and low
        mid = (high + low) // 2  # perform floor division  (ex: 7//2 == 3)

        if lst[mid] == target:
            return mid
        elif target < lst[mid]:  # target is lower than middle value, update high to be mid
            # slice syntax will go up to and including the upper bound, so use list start up to but not including mid
            high = mid - 1
        elif target > lst[mid]:  # target is higher than middle value, use upper half of the list
            # slice syntax will start at and include the lower bound, so use mid + 1 to the end of the list
            low = mid + 1

    # if we don't find the value, return -1
    return -1


def time_search(lst: list, target, search_func):
    """
    Pass lst and target int the provided search_func. Return the
    index returned and the time elapsed when the search was running
    """
    start = time.time()
    ind = search_func(lst, target)
    end = time.time()
    return ind, round((end - start) * 1000, 4)


def main():
    print("=== UNIT 5: SEARCH ALGORITHMS ===")

    # ===============================
    # TODO (Student): SMALL DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a small sorted dataset.
    # 2. Test both linear search and binary search.
    # 3. Search for:
    #    - a value that exists
    #    - a value that does not exist
    # 4. Use comments to clearly explain the results.

    print("\n=== SMALL DATASET TEST ===")
    print("TODO: Create a small dataset and test both searches.")

    nums = [2,5,7,12,14,19,24,28,43,52,70]
    print(f"\nList: {', '.join([str(n) for n in nums])}")

    # search for early value
    val = 12
    print(f"\nSearching for {val}...")
    # expect linear to be faster than binary because it is early in the list, so will check
    # less indices before finding the value
    ind, elapsed = time_search(nums, val, linear_search)
    print(f'  \u2192 Linear Search took {elapsed} milliseconds and returned {ind}.')

    ind, elapsed = time_search(nums, val, binary_search)
    print(f'  \u2192 Binary Search took {elapsed} milliseconds and returned {ind}.')


    # search for last value
    val = 70
    print(f"\nSearching for {val}...")
    # expect binary to be faster than linear because it is the last value in the list, so will check
    # every index for linear search before finding the value, while binary only checks 3 indices
    ind, elapsed = time_search(nums, val, linear_search)
    print(f'  \u2192 Linear Search took {elapsed} milliseconds and returned {ind}.')

    ind, elapsed = time_search(nums, val, binary_search)
    print(f'  \u2192 Binary Search took {elapsed} milliseconds and returned {ind}.')


    # search for nonexistent value
    val = 350
    print(f"\nSearching for {val} (does not exist)...")
    # expect binary to be faster than linear because linear search needs to check all indices
    # in the list to determine the value does not exist, while binary only checks 5 indices
    ind, elapsed = time_search(nums, val, linear_search)
    print(f'  \u2192 Linear Search took {elapsed} milliseconds and returned {ind}.')

    ind, elapsed = time_search(nums, val, binary_search)
    print(f'  \u2192 Binary Search took {elapsed} milliseconds and returned {ind}.')


    # ===============================
    # TODO (Student): LARGE DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a much larger sorted dataset.
    # 2. Test both search algorithms.
    # 3. Compare the results.
    # 4. Use comments to explain why binary search becomes more
    #    efficient as datasets grow larger.

    print("\n=== LARGE DATASET TEST ===")
    print("TODO: Create a larger dataset and compare results.")

    print('\nGenerating a sorted list of 10,000 random values...')
    nums2 = []
    while len(nums2) < 10_000:
        rint = random.randint(1, 100_000)
        if rint not in nums2:
            nums2.append(rint)

    nums2 = sorted(nums2)

    # get 51th value of 10,000
    fifty = nums2[50]
    # get final value of 10,000
    last = nums2[9999]

    # search for early value
    print(f"\nSearching for {fifty}...")
    # with larger datasets, Binary and Linear search may be close in timeframe when
    # searching for data appearling early in the list, but binary may still be faster
    ind, elapsed = time_search(nums2, fifty, linear_search)
    print(f'  \u2192 Linear Search took {elapsed} milliseconds and returned {ind}.')

    ind, elapsed = time_search(nums2, fifty, binary_search)
    print(f'  \u2192 Binary Search took {elapsed} milliseconds and returned {ind}.')


    # search for last value
    print(f"\nSearching for {last}...")
    # expect binary to be faster than linear because it is the last value in the list, so will check
    # every index for linear search before finding the value.
    ind, elapsed = time_search(nums2, last, linear_search)
    print(f'  \u2192 Linear Search took {elapsed} milliseconds and returned {ind}.')

    # Binary search should be MUCH faster here, as it will split the search pool in half
    # with each check it does. While linear search checks len(nums2) values, binary search
    # checks log(len(nums2)) values in the worst case scenario.
    ind, elapsed = time_search(nums2, last, binary_search)
    print(f'  \u2192 Binary Search took {elapsed} milliseconds and returned {ind}.')


    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Single-element list
    # - Value not present
    # - Value at the first position
    # - Value at the last position
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")
    print("TODO: Demonstrate and explain edge cases.")

    # Edge case 1: Empty List
    nums = []

    val = 5
    print(f"\nSearching an **Empty List** for {val} (does not exist)...")
    # Linear search will not even run through the loop with len(lst) == 0
    ind, elapsed = time_search(nums, val, linear_search)
    print(f'  \u2192 Linear Search took {elapsed} milliseconds and returned {ind}.')
    # Binary search on an empty list will start with low = 0, high = -1, which fails
    # the condition on the while loop. So the loop is skipped, and -1 is returned.
    ind, elapsed = time_search(nums, val, binary_search)
    print(f'  \u2192 Binary Search took {elapsed} milliseconds and returned {ind}.')

    # Edge case 1: List contains single element
    nums = [100]

    val = 100
    print(f"\nSearching a **Single-Element List** for {val}...")
    # Linear search will only need to check a single value
    ind, elapsed = time_search(nums, val, linear_search)
    print(f'  \u2192 Linear Search took {elapsed} milliseconds and returned {ind}.')
    # Binary search also only need to check a single val, because low and high are equal
    # on the first loop
    ind, elapsed = time_search(nums, val, binary_search)
    print(f'  \u2192 Binary Search took {elapsed} milliseconds and returned {ind}.')

    val = 5
    print(f"\nSearching a **Single-Element List** for {val} (does not exist)...")
    ind, elapsed = time_search(nums, val, linear_search)
    print(f'  \u2192 Linear Search took {elapsed} milliseconds and returned {ind}.')
    ind, elapsed = time_search(nums, val, binary_search)
    print(f'  \u2192 Binary Search took {elapsed} milliseconds and returned {ind}.')

    # ===============================
    # TODO (Student): REAL WORLD SCENARIO
    # ===============================

    print("\n=== REAL WORLD SCENARIO ===")
    print("TODO: Create a real world scenario.")

if __name__ == "__main__":
    main()

