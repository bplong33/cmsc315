# Unit 4 Discussion: Binary Search Trees

## Overview

This assignment introduces Binary Search Trees (BSTs) and recursive tree operations.

## Learning Objectives

- Build a BST
- Insert values recursively
- Search recursively
- Perform in-order traversal
- Understand BST organization

## Requirements

1. Build a BST.
2. Insert multiple values.
3. Demonstrate in-order traversal.
4. Test searching.
5. Demonstrate edge cases.
6. Create a real-world BST example.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?

I have known about the Tree data type, but have not had many opportunities to use them in any projects I have worked on. The code for this discussion post gave me some good hands on experience with trees, as well as a nice refresher on recursion. Without recursion, Trees could be a bit tedious to use effectively. Specifically, I think it was helpful to go through the process traversing nodes in a tree. When I was first learning about BSTs, I remember being a bit confused when trying to recursively traverse the nodes. This assignment helped to solidify that concept.

2. What challenges did you encounter, and how did you overcome them?

When testing the `search`/`_search_recursive` methods, I ran into a small "issue" of sorts. I was attempting to search for 2 values from the list and 2 values that are not in the list. All values were returning `True`, meaning my function was (I thought) returning the wrong values. I spent some time adding in some logging to help me determine where the error might be.

<img width="727" height="411" alt="unit4 discussion debugging" src="https://github.com/user-attachments/assets/730eec28-9cb1-41bd-a913-f78071669efa" />

After adding this message, I noticed that the output said it was always searching for 4. I checked back to where I was calling the method. I had recently refactored this bit of code to loop through a list of values to search rather than have the same code written 3 times. While doing this, I had forgotten to change the value passed into the search to the variable.

<img width="549" height="325" alt="unit4 discussion err location" src="https://github.com/user-attachments/assets/7f33b4d6-ff8e-45c1-aca2-78a37407d848" />

This ended up being an easy fix. However, it shows how easily small mistakes can throw you off and make you second guess your code. It can be very helpful in this situation to define unit tests that test new features and regression test old features to ensure existing code is not broken by recent changes.

3. Explain BST behavior and compare to how ordering works to create efficiency as compared to other data structures.

Binary Search Trees (BSTs) are ordered from least to greatest. When a new node is added, it is compared against the root node. If it is greater than the root node value, then the right child of the root node is compared. If it is less than the root, the left child of the root node is compared. These comparisons are run at each level of the tree until the traversal finds the "end" of a path. This is where the new node is placed. This means that both node insertion, node removal, and searching are all very efficient. Why is this? If the tree is relatively balanced, then the first comparison against the root node will remove half of the searchable values from the search pool. At the next comparison at level 1 of the tree, the remaining search pool is again cut roughly in half. Lets look at my tree from the earlier as an example, compared against the list that was used to create the tree.

```py
sample_list = [10, 4, 5, 18, 13, 14, 20]
```

```md
      10
     /  \
    4    18
     \   / \
      5 13  20
         \
          14
```

If we were to look for the value 20 in the first list, we would have to iterate over 7 values before we find our target value. With the tree, we only need to check 3 nodes (10, 18, and 20) to find our target value. Checking the first node finds that 20 > 10, and removes 3 values from the pool. Checking the second node finds that 20 > 18, and removes 3 more values from the search pool. Searching the third node finds that 20 == 20, so we have found our value and can return True for the search. Where a typical list or linked list would take O(n) in worst case scenarios, BST searches only take O(h), in worst case scenarios, where *h* is the height of the tree.
