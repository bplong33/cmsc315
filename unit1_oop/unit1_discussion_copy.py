"""
===========================================================
Unit 1 DISCUSSION: Python OOP, Namespaces, and Copying
===========================================================

INSTRUCTIONS:
In this assignment, you will build and explore object-oriented programming (OOP) concepts in Python.
You are provided with starter code containing TODO sections. Your task is to complete, modify, and
analyze the code to demonstrate understanding of inheritance, namespaces, and object copying.
"""

from copy import copy, deepcopy


# TODO 1:
# Create a parent class.
#
# Requirements:
# - Include at least one class variable.
# - Include at least two instance variables.
# - Include a constructor (__init__).
# - Include a method that returns or displays information about the object.
#
# Replace the pass statement with your implementation.


class Media:
    TOTAL_MEDIA_COUNT = 0

    def __init__(self, title: str, year: int, genre: str):
        self._title = title
        self._year = year
        self._genre = genre
        # increment the count of media objects that were created
        self.TOTAL_MEDIA_COUNT += 1

    def about(self) -> None:
        print(f"Title: {self._title}\nRelease Year: {self._year}\nGenre: {self._genre}")

    @classmethod
    def get_media_count(cls) -> int:
        return cls.TOTAL_MEDIA_COUNT


# TODO 2:
# Create a child class that inherits from the parent class.
#
# Requirements:
# - Use inheritance.
# - Add at least one new class variable.
# - Add at least two new instance variables.
# - Add at least one new method.
# - Override a method from the parent class.
#
# Replace the pass statement with your implementation.


class Game(Media):
    MEDIA_TYPE = "Video Game"

    def __init__(self, title: str, year: int, genre: str, rating: str):
        super().__init__(title, year, genre)
        if rating.upper() in ["E", "T", "M", "NR"]:
            self._rating = rating
        else:
            self._rating = "NR"

    def about(self) -> None:
        super().about()
        print(f"Rating: {self._rating}")


# TODO 3:
# Create a function that demonstrates class namespaces and instance namespaces.
#
# Your function should:
# - Create at least two objects of the child class.
# - Access a class variable through the class itself.
# - Access the same class variable through an object.
# - Add a new attribute to only one object after it is created.
# - Display each object's namespace using __dict__.
# - Display information about the class namespace.


def demonstrate_namespaces():
    print("\n=== Namespace Demonstration ===")
    print("\nTODO: Implement namespace demonstration")

    # 2 Child Class Objects
    print("\nCreating child object `game1`...\n")
    game1 = Game("Elden Ring", 2022, "Souls-like", "M")
    game1.about()
    print("\nCreating child object 2 `game2`...\n")
    game2 = Game("The Division 2", 2019, "Looter Shooter", "M")
    game2.about()

    print(
        f"\nDisplaying child class variable (via Class):\n\tGame: MEDIA_TYPE: {Game.MEDIA_TYPE}"
    )
    print(
        f"\nDisplaying child class variable (via instance object):\n\tgame1: MEDIA_TYPE: {game1.MEDIA_TYPE}"
    )
    print("\nAdding `review` attribute to game2...")

    game2.review = "79% Recommended"

    print("Displaying each child object's namespace...\n")
    print("game1:")
    print(game1.__dict__)
    print("game2:")
    print(game2.__dict__)

    print(
        "\nNotice that the `game2` object has `review` attribute, which `game1` does not."
    )


# TODO 4:
# Create a function that demonstrates shallow copying and deep copying.
#
# Requirements:
# - Create an object that contains nested mutable data.
# - Create a shallow copy.
# - Create a deep copy.
# - Modify the original object's nested data.
# - Display the original object, shallow copy, and deep copy.
# - Use comments to explain the difference between shallow and deep copying.


def demonstrate_copying():
    print("\n=== Copy Demonstration ===")
    print("TODO: Implement shallow copy and deep copy demonstration")


# TODO 5:
# Complete the main function.
#
# Requirements:
# - Create at least one object from the parent class.
# - Create at least one object from the child class.
# - Demonstrate inheritance by calling methods.
# - Call your namespace demonstration function.
# - Call your copy demonstration function.


def main():
    print("=== Unit 1 OOP Assignment ===")

    print("\nTODO: Create and test your parent object\n")
    m1 = Media("Spiderman: Brand New Day", 2026, "Action/Adventure")
    m1.about()

    print("\nTODO: Create and test your child object\n")
    game1 = Game("Elden Ring", 2022, "Souls-like", "M")
    game1.about()
    print(
        "\nMedia Count should be 2, as we have created two objects (parent and child) that both would "
        + "have incremented the count. Note that the method used to get the media count is inherited "
        + f"from the parent class, as is the class variable:\n  Count: {game1.get_media_count()}"
    )

    demonstrate_namespaces()
    demonstrate_copying()


if __name__ == "__main__":
    main()

