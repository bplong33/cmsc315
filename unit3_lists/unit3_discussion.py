"""
==================================================
Unit 3 DISCUSSION: List Operations (Insert, Delete, Search)
==================================================

INSTRUCTIONS:
This assignment focuses on understanding how lists behave when elements
are inserted, removed, and searched. You will analyze how Python lists
shift elements in memory and how different operations impact performance.
"""


def insert_at(lst: list, index, value):
    """
    TODO (Student):
    Insert a value into the list at the specified index.

    Requirements:
    - Use a list operation to insert the value.
    - Add comments explaining what happens to existing elements
      after an insertion occurs.
    - Use comments to explain how insertion performance may vary depending on
      where the insertion occurs.
    """
    # Insert at provided index, pushing other list elements to the right by 1 index if they fall on or after the specified index
    # Inserting closer to the front (index 0) will take more time than inserting into a later index.
    # More values will need to be moved when inserting into the front
    lst.insert(index, value)
    # Notice that no value needs to be returned. Python passes a *reference* of the list to the
    # function, so the original list is updated.


def delete_at(lst: list, index: int):
    """
    TODO (Student):
    Remove and return the value at the specified index.

    Requirements:
    - Validate that the index exists.
    - Return the removed value.
    - Return None if the index is invalid.
    - Add comments explaining why index validation and safe deletion are important.
    """
    # Verify the index is within the valid range of the list.
    # Failing to verify would result in out function throwing exceptions
    # when provided with an invalid value
    if 0 <= index < len(lst):
        # pop accepts an index argument, removing the item and returning it
        return lst.pop(index)
    return None


def search_value(lst: list, value):
    """
    TODO (Student):
    Search for a value within the list.

    Requirements:
    - Return the index if the value is found.
    - Return -1 if the value is not found.
    - Add comments explaining why this is a linear search and why it scans sequentially.
    """
    # Use try except block because the list `.index(value)` will throw an exception if
    # the provided value is not fount
    try:
        # The list is searched from index 0 to the last index, checking the value at each
        # index to see if it matches the provided value
        return lst.index(value)
    except ValueError:
        # return -1 if the value was not found in the list
        return -1


def main():
    print("=== UNIT 3: LIST OPERATIONS ===")

    # ===============================
    # TODO (Student): INSERTION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Create a list containing several values.
    # 2. Display the original list.
    # 3. Test insertion at:
    #    - the beginning
    #    - the middle
    #    - the end
    # 4. Display the list after each insertion.
    # 5. Use comments to explain each step in the implementation.

    print("\n=== INSERTION TESTS ===")
    print("TODO: Create a list and demonstrate insertions.")

    # create original list
    l1 = ["Sara", "Finley"]
    # display list
    print(f"\nOriginal List: {l1}")

    # insert at the beginning (shifts all current values to the right)
    insert_at(l1, 0, "Brandon")
    print(f"List after insert 1: {l1}")

    # insert in the middle (shift "Finley" to the right)
    insert_at(l1, 2, "Oliver")
    print(f"List after insert 2: {l1}")

    # insert at the end (no shifts should occur, best case scenario for efficieny)
    # Using an index matching the length of l1 ensures we place the value at the end, no matter the
    # list size
    insert_at(l1, len(l1), "Emmy")
    print(f"List after insert 3: {l1}")

    # ===============================
    # TODO (Student): DELETION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Delete an item from:
    #    - the beginning
    #    - the middle
    #    - the end
    # 2. Display the removed value.
    # 3. Display the updated list after each deletion.
    # 4. Use comments to clearly explain what is happening in the output.

    print("\n=== DELETION TESTS ===")
    print("TODO: Demonstrate deletions from multiple positions.")

    # display list
    print(f"\nDisplay Current List: {l1}")

    # delete from the beginning
    delete_at(l1, 0)
    print(f"List after deletion 1: {l1}")

    # delete from the middle
    delete_at(l1, 2)
    print(f"List after deletion 2: {l1}")

    # delete from the end
    delete_at(l1, len(l1) - 1)
    print(f"List after deletion 2: {l1}")

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for a value that exists.
    # 2. Search for a value that does not exist.
    # 3. Display the search results with clear explanations.
    # 4. Use comments to explain each step.

    print("\n=== SEARCH TESTS ===")
    print("TODO: Demonstrate searching for values.")

    # display list
    print(f"\nDisplay Current List: {l1}")

    # search for a value that we know exists
    result_ind = search_value(l1, "Oliver")
    print(f"Searching for 'Oliver' returns: {result_ind}")

    # search for a value that does not exist
    result_ind = search_value(l1, "Jeffrey")
    print(f"Searching for 'Jeffrey' returns: {result_ind}")
    print("  \u2192 'Jeffrey' does not exist in the list")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Delete using an invalid index
    # - Search for a missing value
    # - Insert into an empty list
    # - Delete from an empty list
    # - Use comments to explain each edge case.

    print("\n=== EDGE CASES ===")
    print("TODO: Demonstrate at least two edge cases.")

    # Insert to an index greater than the list length
    # display list
    print("\n== Insert into index greater than list length ==\n")
    print(f"Display Current List: {l1}")
    print("Attempt inserting 'Zack' into index 10 when list length is 2")
    insert_at(l1, 10, "Zack")
    print(f"  \u2192 'Zack' added to end of list: {l1}")

    # Detele at negative index
    # display list
    print("\n== Provide a negative index to the delete_at method ==\n")
    print(f"Display Current List: {l1}")
    del_return = delete_at(l1, -2)
    print(
        f"Delete from index -2 returns {del_return} because the index is out of the\n  valid range (0 <= i < len(list))"
    )

    # ===============================
    # TODO (Student): REAL WORLD SCENARIO
    # ===============================

    print("\n=== REAL WORLD SCENARIO ===")
    print("TODO: Create a real world scenario.")

    # Create reusable function to display the SCRUM board
    def display_scrum(lanes: dict[str, list[str]]):
        for lane, lst in lanes.items():
            print(f"  {lane}: {lst}")

    # Represent a SCRUM Board's lanes
    # Used a dictionary for simplified accessing, but the list in dict values will function the same
    lanes = {"Backlog": [], "In Progress": [], "Under Review": [], "Done": []}

    # Display current tickets
    print(
        "A basic SCRUM Board has 4 lanes (Backlog, In Progress, Under Review, and Done). All Lanes start off empty:"
    )
    display_scrum(lanes)

    # Add 3 tickets to the backlog
    insert_at(
        lanes["Backlog"],
        len(lanes["Backlog"]),
        "Add API stubs for CRUD Operations [Pri: Low]",
    )  # add to end of list
    insert_at(
        lanes["Backlog"],
        0,
        "Update package versions [Pri: High]",
    )  # add to beginning of list
    insert_at(
        lanes["Backlog"],
        1,
        "Implement basic FastAPI routing [Pri: Medium]",
    )  # add to middle of list

    print("\nTickets have been added to the Backlog lane:")
    display_scrum(lanes)

    print(
        "\nThe ticket at index 0 (high priority ticket) is worked first, so it is pulled into the In Progress lane"
    )
    # Find which index holds this ticket
    ticket_ind = search_value(lanes["Backlog"], "Update package versions [Pri: High]")
    print(f"  \u2192 Ticket is found at index: {ticket_ind}\n")
    # Delete the value from backlog, returning it
    val = delete_at(lanes["Backlog"], ticket_ind)
    # Add the value to 'In Progress'
    insert_at(lanes["In Progress"], 0, val)

    print("SCRUM Board after update")
    display_scrum(lanes)

    print(
        "\nThe following operations will be completed in the following order:\n  \u2192 Start Low-priority "
        + "ticket\n  \u2192 Start Medium-priority ticket\n  \u2192 Move High and Medium Priority tickets to "
        + "Under Review\n  \u2192 Move High-priority ticket to Done"
    )
    # "Add API stubs for CRUD Operations [Pri: Low]"
    # "Implement basic FastAPI routing [Pri: Medium]",
    # "Update package versions [Pri: High]",

    # Find index, remove from current lane, and insert into next lane
    ticket_ind = search_value(
        lanes["Backlog"], "Add API stubs for CRUD Operations [Pri: Low]"
    )
    val = delete_at(lanes["Backlog"], ticket_ind)
    insert_at(lanes["In Progress"], len(lanes["In Progress"]), val)  # insert at end

    ticket_ind = search_value(
        lanes["Backlog"], "Implement basic FastAPI routing [Pri: Medium]"
    )
    val = delete_at(lanes["Backlog"], ticket_ind)
    insert_at(lanes["In Progress"], 1, val)  # insert in between high and low pri ticket

    # Display SCRUM board after all tickets have been moved out of backlog
    print("\nSCRUM Board after first 2 updates:")
    display_scrum(lanes)

    # Move high and medium priority tickets to under review
    ticket_ind = search_value(
        lanes["In Progress"], "Implement basic FastAPI routing [Pri: Medium]"
    )
    val = delete_at(lanes["In Progress"], ticket_ind)
    insert_at(lanes["Under Review"], len(lanes["Under Review"]), val)  # insert at end

    ticket_ind = search_value(
        lanes["In Progress"], "Update package versions [Pri: High]"
    )
    val = delete_at(lanes["In Progress"], ticket_ind)
    insert_at(lanes["Under Review"], 0, val)  # insert at beginning

    # Display SCRUM board after 2 tickets have been moved to under review
    print("\nSCRUM Board after third update:")
    display_scrum(lanes)

    # Move high priority ticket to Done
    ticket_ind = search_value(
        lanes["Under Review"], "Update package versions [Pri: High]"
    )
    val = delete_at(lanes["Under Review"], ticket_ind)
    insert_at(lanes["Done"], 0, val)  # insert at beginning

    # Display SCRUM board after all operations have been performed
    print("\nSCRUM Board final state:")
    display_scrum(lanes)


if __name__ == "__main__":
    main()

