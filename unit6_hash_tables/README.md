# Unit 6 Discussion: Dictionaries as Hash Tables

## Overview

This assignment uses Python dictionaries to demonstrate hash table behavior.

## Learning Objectives

- Insert key-value pairs
- Retrieve values efficiently
- Update existing values
- Remove entries
- Understand hashing concepts

## Requirements

1. Create and populate a dictionary.
2. Demonstrate lookup operations.
3. Demonstrate update operations.
4. Demonstrate delete operations.
5. Test edge cases.
6. Create a real-world scenario.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?

The biggest takeaway for me from this assignment was gaining a deeper understanding of how dictionaries and hash tables actually perform under the hood. I have used python dictionaries for many years, but never understood why they are efficient or how they determine key placement, retrieval, etc. This assignment pushed me to look into the inner workings of python dictionaries and truly understand how they work.

2. What challenges did you encounter, and how did you overcome them?

As I mentioned in the previous section, I have used dictionaries for often in my years as a developer. My biggest challenge was trying to understand how Python specifically implements their dictionaries, to include their collision handling, probing process, insertion mechanisms, and how all of these work together to make dictionaries one of Python's most useful and efficient data structures.

3. Explain how hash tables behave, what collisions are, and how hash tables can improve efficiency.

Hash tables function based on every entry have a key-value pair. The key for each value is *hashed*, using a hashing algorithm determined for the type of key. The hash that is output by the hashing algorithm is used to determine what index in the hash table the key and value will be stored at. Hashing a key does not mean that the index chosen is unique to that key. Multiple keys may result in a hash that points to the same index of the hash table. This is considered a collision. There are multiple methods of handling collisions, such as chaining and open addressing.

A hash table does not have to search linearly, but instead searches based on the initial hash value of the key and the probing process selecting when the hash table is designed. This means that the index that the value should be is found in near constant time via the hashing process. In the case of collisions, the number of follow on probes may vary depending on how full the hash table is. Regardless, this implementation averages out to nearly constant time operations (O(1)) for search, retrieval, insertion, and deletion operations for hash tables. When using a hash table makes sense, it is usually the most efficient option.
