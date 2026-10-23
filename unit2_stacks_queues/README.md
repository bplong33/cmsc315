# Unit 2 Discussion: Stacks and Queues

## Overview

This assignment explores two fundamental linear data structures:

- Stack (LIFO)
- Queue (FIFO)

## Learning Objectives

- Implement stack operations
- Implement queue operations
- Understand LIFO and FIFO behavior
- Create edge cases

## Requirements

Complete all TODO sections:

1. Implement stack operations.
2. Implement queue operations.
3. Demonstrate LIFO behavior.
4. Demonstrate FIFO behavior.
5. Create and test edge cases.
6. Create a real-world scenario.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?

I have used lists and dictionaries very often throughout my time coding. However, the use of stacks and queues demonstrates these same or similar data types being used in specific use cases in very intentional ways. While completing this project, it was very helpful to contextualize why you may choose to use each one of these data structures. I also though it was interesting to see that, although there are built-in data types (lists) and modules available (dequeue), custom implementations of these give the developer a lot of room to build upon how the data structure is used and define its specific behavior. I have used lists as a basic stack many times, but I have never defined a class around managing that list in a specific way.

2. What challenges did you encounter, and how did you overcome them?

One challenge I ran into was an improper use of the pop/dequeue methods within my real world scenario. In the while loop where I iterate through the textbook stack and student queue, I initially was using the pop and dequeue method to populate the `nxt_book` and `nxt_student` variables. This worked fine, until one of the objects was empty. In this situation, it would pull the correct data from one, but return `None` for the other. This was not the intended functionality, as it would remove the last student from the student queue, even though that student had not been provided with a textbook.

```diff
    while True:
-       nxt_student = student_queue.pop()
-       nxt_book = textbook_inventory.dequeue()
+       nxt_student = student_queue.front()
+       nxt_book = textbook_inventory.peek()
        if nxt_student and nxt_book:
-           print(
-               f"  {nxt_student} has been assingned textbook {nxt_book}"
-           )
+           print(
+               f"  {student_queue.dequeue()} has been assingned textbook {textbook_inventory.pop()}"
+           )
        elif not nxt_student:
            print("All students have been provided with a textbook")
            break
        else:
            print("  \n******\nWARNING: No more textbooks in inventory\n******\n")
            break

```

After noticing this, I change changed the assignments to use peek() and front() in order to get the value without removing them. Then, I check if either was empty, and only pop/dequeue if a value is returned from both the stack and the queue.

3. Explain the differences between stacks and queues as this relates to real-world applications.

Stacks are useful in situations where you want to remove or process items starting with the last item that was added, while Queues are useful when you want to process items specifically in the order that they are received. This makes the stack an ideal data type for uses such as recording actions that were taken in a software, which can then be popped from the stack to undo the action. Queues, on the other hand, are great for chronologically processing requests or events in the order they occurred.
