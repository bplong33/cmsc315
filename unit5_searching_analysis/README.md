# Unit 5 Discussion: Search Algorithms

## Overview

This assignment compares linear search and binary search.

## Learning Objectives

- Implement linear search
- Implement binary search
- Compare performance
- Analyze algorithm efficiency

## Requirements

1. Test both algorithms on a small dataset.
2. Test both algorithms on a large dataset.
3. Demonstrate edge cases.
4. Analyze performance.
5. Create a real-world search scenario.


## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?

While working on this assignment, I gained a better understanding of Binary Search as it applies to lists, along with an improved understanding of when to use binary search. I have a habit of using default Python lists and using the list's build-in methods to search for values. I realize now that I may need to re-evaluate some list implementations in order to improve performance within the programs.  

2. What challenges did you encounter, and how did you overcome them?

When I initially implemented the binary search function, I was attempting to do it through recursion. It wasn't until I was testing that I realized the method would find the value, but would always return the incorrect index holding the searched value. When sending the sub-list to the recursive function, I was using python slice syntax to grab the appropriate chunk of the list to continue searching. By the time the list had found the value, the indices of the lists send into the recursive function call were different from the base list's indices.

Overcoming this simply meant switching to use a while loop to run the binary search rather than recursion. In order for recursion to work, the method would need to accept a high and low value as arguments. This would allow the recursive calls to know the appropriate starting and ending search ranges, without changing the indices that the search is referencing. However, switching to the while loop was not too difficult.

3. Explain when to use linear versus binary search, including tradeoffs in real-world scenarios.

On smaller datasets, it is typically safe to use linear search, while binary search is better to use for larger datasets. However, there is more nuance to the conversation than this statement. For example, we should consider if the use case is a one-off script, if the scale of the application will require many users searching at once, and if the list of values already sorted. It may be acceptable for a one-off script to take slightly longer to run while using a linear search. Similarly, if the data is not sorted, then a binary search is not an option unless the data were to be sorted first. Searching data with less than 10,000 data points in a linear fashion is relatively fast. However, data having around 10,000 to 100,000 data points should be considered for use with a binary search. Additionally, we should consider how many users may be trying to search the data. If many users are attempting to run searches simultaneous, the "slightly" longer search time from linear searches may begin to add up to be very inefficient code. I would argue that for *sorted* datasets of moderate length (~5k - 10k), it would be wise to use a binary search.
