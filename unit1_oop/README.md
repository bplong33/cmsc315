# Unit 1 Discussion: Python OOP, Namespaces, and Copying

## Overview

This assignment explores object-oriented programming (OOP) concepts in Python, including inheritance, namespaces, and object copying.

## Learning Objectives

- Create parent and child classes
- Use inheritance to extend functionality
- Understand class and instance namespaces
- Demonstrate shallow and deep copying
- Apply object-oriented design principles

## Requirements

Complete all TODO sections in the source code:

1. Create a parent class.
2. Create a child class using inheritance.
3. Demonstrate class and instance namespaces.
4. Demonstrate shallow and deep copying.
5. Create and test objects in `main()`.
6. Add a student-created extension.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?

I have worked with Object Oriented Programming concepts in some of my previous positions and applications, so much of this first week was a great refresher for these concepts. However, I think the lesson that I found most beneficial from this assignment was gaining a deeper understanding of shallow vs deep copying in Python. I distinctly remember encountering issues or confusion related to this, where I intended to make a copy of a list to modify or track during a for loop iteration. The implementation caused errors because both variables were referencing the same object, which was constantly being modified. Having a deeper understanding of how this works will help to prevent errors like this in the future.

2. What challenges did you encounter, and how did you overcome them?

As far as challenges, my biggest challenge was attempting to format the output in a pleasing way. Also, I had a moment of confusion when attempting to increment the class variable I set on my parent class. My goal was to set a class variable on the Parent class that would increment with each instance of the parent and child class. Initially, I was running `self.media_count += 1` in the Media class' `__init__`. However, in order to fix this, I needed to reference the class variable by doing `Media.media_count += 1`. Overall, this was a very simple fix.

3. Compare OOP to procedural programming.

Procedural Programming and Object Oriented Programming techniques are quite different. Procedural Programming involves writing code in the sequential order that it should be executed in. With object oriented programming, rather than thinking of the code as a set of steps or operations, you can instead think of the problem as a collection of objects, each with it's own set of behaviors and defining characteristics. You can then define how these objects interact with other objects. For many use cases, thinking about code in this way is often much more natural and intuitive than procedural programming.

4. Discuss the benefits of maintainability and reusability and apply this managing overhead, practical application development, and future use.

A well designed set of classes can make developing and maintaining an application significantly easier. If a piece of code, a specific value, or a general design structure is repeated throughout a file or code base, any update to one instance would require an update to all of the others as well. Implementing these as a Global variable or function can make it much easier to perform these updates, as you can make the update in one place and all references to it will pick up the updates. OOP design extends this even more, allowing you to wrap complex interactions of an object (or between objects) within the definition of a collection of classes. It is much easier to maintain and update an objects behavior in a single place, rather than update it anywhere that the object is instantiated and used.
