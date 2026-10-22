"""
===========================================================
UNIT 2 DISCUSSION: STACKS AND QUEUES (PYTHON)
===========================================================

OVERVIEW:
This assignment introduces two fundamental data structures:
the Stack (LIFO) and the Queue (FIFO).

You will complete, modify, and extend the starter code while
explaining key concepts through comments and improved output.
"""

from collections import deque


class Stack:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the stack.
        # Hint: A Python list can be used to store stack values.
        self.data = []

    def push(self, value):
        # TODO (Student): Add value to the stack.
        # Add a short comment explaining why this operation supports LIFO behavior.

        # Add the provided value to the END of the list. We can later use a .pop() method to pull
        # the last value off of the list.
        self.data.append(value)

    def pop(self):
        # TODO (Student): Remove and return the most recently added value.
        # Improve or explain empty-stack handling.
        # What should happen if the stack is empty?

        # only run .pop() if the stack has data. If we try to pop with no data, we will get
        # an exception. If data is empty, return None.
        return None if self.is_empty() else self.data.pop()

    def peek(self):
        # TODO (Student): Return the top value without removing it.
        # Add a comment explaining what peek does.

        # if the stack has data, return the last element in the list, which is the top of the stack.
        # If stack is empty, return None
        return None if self.is_empty() else self.data[-1]

    def is_empty(self):
        # TODO (Student): Return True if the stack has no values.

        # Return false if the length of the stack is > 0, otherwise return false
        return False if len(self.data) else True


class Queue:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the queue.
        # Hint: collections.deque is useful for efficient queue operations.
        self.queue = deque()

    def enqueue(self, value):
        # TODO (Student): Add value to the back of the queue.
        # Add a short comment explaining why this operation supports FIFO behavior.

        # Add the provided value to the end of the queue (back of the "line"). If we pull
        # from the front of the queue (i.e. index 0), this added item will be the last retrieved.
        # This means the first values appended will be the first items retrieved
        self.queue.append(value)

    def dequeue(self):
        # TODO (Student): Remove and return the value from the front of the queue.
        # Explain or improve empty-queue handling.

        # If the queue has data, pop the leftmost value (the FIRST value, at the front of the queue)
        # from the queue and return. Else, return None
        return None if self.is_empty() else self.queue.popleft()

    def front(self):
        # TODO (Student): Return the front value without removing it.
        # Add a comment explaining what front returns.

        return None if self.is_empty() else self.queue[0]

    def is_empty(self):
        # TODO (Student): Return True if the queue has no values.

        # Return false if the length of the queue is > 0, otherwise return false
        return False if len(self.queue) else True


def main():
    print("=== UNIT 2: STACKS AND QUEUES ===")

    # ===============================
    # TODO (Student): STACK DEMO
    # ===============================
    # Requirements:
    # 1. Create a Stack object.
    # 2. Add at least 4 values to the stack.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate LIFO behavior.
    # 5. Show what happens when pop() is used on an empty stack.
    #
    # Edge Cases:
    # 6. Show what happens when peek() is used on an empty stack.
    # 7. Create a stack with only one item, remove it,
    #    and verify the stack is empty afterward.

    print("\n=== STACK DEMO ===\n")

    print("Creating a stack object...")
    stk = Stack()
    print(f"  Stack: {stk.data}\n")

    print("Adding 5 items to the stack, in the order shown: 27, 7, 6, 30, 4")
    stk.push(27)
    stk.push(7)
    stk.push(6)
    stk.push(30)
    stk.push(4)

    print("The stack now holds the following data:")
    print(f"  Stack: {stk.data}\n")

    print(
        "Popping from the stask should remove the last item, so in order, pop should\n"
        + "return 4, 30, 6, 7, 27: \n"
    )
    print(
        f"  {stk.pop()}\n  {stk.pop()}\n  {stk.pop()}\n  {stk.pop()}\n  {stk.pop()}\n"
    )
    print("The stack is now empty:\n")
    print(f"  Stack: {stk.data}\n")

    print("Now, popping and peeking from an empty stack should return None:\n")
    print(f"  Peek demo: {stk.peek()}")
    print(f"  Pop demo: {stk.pop()}\n")

    stk2 = Stack()
    stk2.push("Hello")
    print(f"If we have a stack with only a single item...\n  Stack 2: {stk2.data}\n")
    print("Popping this last item should leave an empty stack:")
    print(f"  Popped item: {stk2.pop()}")
    print(f"  Stack after pop: {stk2.data}")

    # ===============================
    # TODO (Student): QUEUE DEMO
    # ===============================
    # Requirements:
    # 1. Create a Queue object.
    # 2. Add at least 4 values to the queue.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate FIFO behavior.
    # 5. Show what happens when dequeue() is used on an empty queue.
    #
    # Edge Cases:
    # 6. Show what happens when front() is used on an empty queue.
    # 7. Create a queue with only one item, remove it,
    #    and verify the queue is empty afterward.

    print("\n=== QUEUE DEMO ===\n")

    print("Creating a queue object...")
    que = Queue()
    print(f"  Queue: {que.queue}\n")

    print("Adding 5 items to the queue, in the order shown: 27, 7, 6, 30, 4")
    que.enqueue(27)
    que.enqueue(7)
    que.enqueue(6)
    que.enqueue(30)
    que.enqueue(4)

    print("The queue now holds the following data, with 27 at the front of the queue:")
    print(f"  Queue: {que.queue}\n")

    print(
        "Dequeueing from the queue should remove the items in the order they were added,\n"
        + "so in order, dequeue should return 27, 7, 6, 30, 4: \n"
    )
    print(
        f"  {que.dequeue()}\n  {que.dequeue()}\n  {que.dequeue()}\n  {que.dequeue()}\n  {que.dequeue()}\n"
    )
    print("The queue is now empty:\n")
    print(f"  Queue: {que.queue}\n")

    print(
        "Now, dequeueing and looking at the front of an empty queue should return None:\n"
    )
    print(f"  Front demo: {que.front()}")
    print(f"  Dequeue demo: {que.dequeue()}\n")

    que2 = Queue()
    que2.enqueue("Hello")
    print(f"If we have a queue with only a single item...\n  Queue 2: {que2.queue}\n")
    print("Dequeueing this item should leave an empty queue:")
    print(f"  Dequeued item: {que2.dequeue()}")
    print(f"  Queue after dequeue: {que2.queue}")


if __name__ == "__main__":
    main()
