# Unit 3 Discussion: List Operations

## Overview

This assignment examines insertion, deletion, and searching in Python lists.

## Learning Objectives

- Insert values into a list
- Delete values from a list
- Search for values in a list
- Analyze list behavior and performance

## Requirements

1. Test insertion at the beginning, middle, and end.
2. Test deletion at the beginning, middle, and end.
3. Search for existing and missing values.
4. Demonstrate edge cases.
5. Create a real-world scenario.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?

Through this assignment, I learned that using the python list's `index(<value>)` method to search for a value in a list will actually raise an error if the value is not found. Historically, I have either used something like `if val in list1` to check if a value is in the list, but this would not return an index. Alternatively, I've used a for loop in the past to iterate through the list to look for a value. This is what is happening when using the `index()` method. However, I haven't used the built-in method to search for the index of a value. When first implementing it, I expected it to return None or -1 as a default if a value was not found. I was surprised to find that it Raises a `ValueError`.

2. What challenges did you encounter, and how did you overcome them?

While building my real-world scenario, I was faced with a lot of scope creep. I had the initial idea of replicating basic SCRUM Board functionality of changing the status on tickets. As I was working, I had a few ideas of how to improve upon it, like building a function to move a given ticket from its current list to provided one, or sorting lists by priority. I considered creating a class for the board, and another for the lanes, which would allow for more granular control over the behavior. These are all things I would have implemented if this were a larger project, but for the purposes of demonstrating list insertion, deletion, and searching, it felt a bit excessive to create so many parts. This is something that developers often face in the real world. Often, work is scoped to include specific development tasks, and it is easy to have the scope of work grow beyond the planned work. 

3. How do list operations impact performance in real-world applications?

List operations, specifically with Python array lists, can vary depending on the size of the list and the task being performed. It is important to choose the right data type for the job, otherwise you risk reducing the performance of the application. For example, searching an array in python typically requires checking each index, starting at index 0, until you find the item being searched for. If the list is long and the item being searched is at the end, this can take a very long time. Other options of searching or other list types may improve performance. Similarly, using a Linked List structure removes the ability to access a specific index of a list the way you can in a Pythonic list. Weighting the importance of features such as insertion/deletion, searching, sorting, resizing, and scalability may impact which data type we would choose to use.
