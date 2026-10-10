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
    media_count: int = 0

    def __init__(self, title: str, year: int, genre: str):
        self._title = title
        self._year = year
        self._genre = genre
        # increment the count of media objects that were created
        Media.media_count += 1

    def about(self) -> None:
        print(f"Title: {self._title}\nRelease Year: {self._year}\nGenre: {self._genre}")

    @classmethod
    def get_media_count(cls) -> int:
        return cls.media_count


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

    def __init__(
        self, title: str, year: int, genre: str, rating: str, platforms: list[str]
    ):
        super().__init__(title, year, genre)
        if rating.upper() in ["E", "T", "M", "NR"]:
            self._rating = rating
        else:
            self._rating = "NR"

        self._platforms = platforms

    def about(self) -> None:
        super().about()
        print(f"Rating: {self._rating}\nPlatforms: {[', '.join(self._platforms)]}")


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
    game1 = Game("Elden Ring", 2022, "Souls-like", "M", ["PC", "Xbox", "PS"])
    game1.about()
    print("\nCreating child object 2 `game2`...\n")
    game2 = Game("The Division 2", 2019, "Looter Shooter", "M", ["PC", "PS"])
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
    print("\ngame2:")
    print(game2.__dict__)

    print(
        "\nNotice that the `game2` object has `review` attribute, which `game1` does not."
    )

    print(f"\n`Game` Class Information:\n{Game.__dict__}")


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

    orig = [{"a": 3}, {"b": 9}, {"c": 3}, {"d": 1}]
    print(f"\nCreated original collection:\n\n  {orig}")
    cp = orig
    print(
        f"\nSet new variable with `cp = orig` (references the same list object):\n\n  {cp}"
    )
    cp[1] = {"b": 8}
    print(
        '\nNow, updating `cp` will also update `orig`. After running `cp[1] = {"b": 8}`, '
        + f"both objects have been modified:\n\n  original: {orig}\n  cp: {cp}"
    )

    # Shallow Copy
    print("\n---\nReset original and perform shallow copy...\n")
    orig = [{"a": 3}, {"b": 9}, {"c": 3}, {"d": 1}]
    cp = copy(orig)
    cp[3] = {"test": "orig shouldn't change"}
    print(
        "When replacing an entire index of cp, the original shouldn't change because we are\npointing the copy to a new object reference:\n"
    )
    print(f"  original: {orig}\n  cp: {cp}")

    cp[1]["b"] = 8
    print(
        "\nHowever, if we update a nested value of the object at an index, such as updating a key\n"
        + "in the dictionary at index 1, then we are updating the object that the original is still\n"
        + "pointing to as well, meaning both will be updated (shallow copy).\n"
    )
    print(f"  original: {orig}\n  cp: {cp}")

    # Deep Copy
    print("\n---\nReset original and perform deep copy...\n")
    orig = [{"a": 3}, {"b": 9}, {"c": 3}, {"d": 1}]
    cp = deepcopy(orig)
    cp[1]["b"] = 8
    print(
        "With a deep copy, even when changing nested values in either list, the indices in both\n"
        + "objects are pointing to different references for the objects they are hold, so\n"
        + "updates will only affect one object.\n"
    )
    print(f"  original: {orig}\n  cp: {cp}")


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
    print("\nMedia Count: ", m1.get_media_count())

    print("\nTODO: Create and test your child object\n")
    game1 = Game("Elden Ring", 2022, "Souls-like", "M", ["PC", "Xbox", "PS"])
    game1.about()
    print("\nMedia Count: ", game1.get_media_count())
    print(
        "\nMedia Count should be 2, as we have created two objects (parent and child) that both would "
        + "have incremented the count. Note that the method used to get the media count is inherited "
        + f"from the parent class, as is the class variable:\n  Count: {game1.get_media_count()}"
    )

    demonstrate_namespaces()
    demonstrate_copying()


if __name__ == "__main__":
    main()
