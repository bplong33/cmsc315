"""
=========================================================
UNIT 4 DISCUSSION: BINARY SEARCH TREES (BST)
=========================================================

INSTRUCTIONS:
This assignment focuses on understanding and implementing a
Binary Search Tree (BST).

You will complete and modify the provided code while explaining
key concepts in your own words using comments and output.
"""


class Node:
    def __init__(self, value):
        # TODO (Student):
        # Store the node's value and initialize references
        # to the left and right child nodes.
        self.value = value
        self.left: Node | None = None
        self.right: Node | None = None


class BST:
    def __init__(self):
        # TODO (Student):
        # Initialize an empty Binary Search Tree.
        self.root = None
        self.size = 0  # added to track count of values in the tree

    def insert(self, value):
        """
        TODO (Student):
        Insert a value into the BST.

        Requirements:
        - Use the recursive helper method.
        - Add comments explaining why insertion depends on
          whether a value is smaller or larger than the
          current node.
        """
        # TODO: Handle situation where new value is already in the tree
        if self.root is None:
            self.root = Node(value)
            self.size += 1
            return self.root
        else:
            return self._insert_recursive(self.root, value)

    def _insert_recursive(self, parent: Node, value):
        """
        TODO (Student):
        Implement recursive BST insertion.

        Requirements:
        - Create a new node when a position is found.
        - Insert smaller values into the left subtree.
        - Insert larger values into the right subtree.
        - Return the updated node reference.
        """
        if value < parent.value:
            if parent.left is None:
                newNode = Node(value)
                parent.left = newNode
                self.size += 1  # new node added, increment size
                return newNode
            else:
                return self._insert_recursive(parent.left, value)
        if value > parent.value:
            if parent.right is None:
                newNode = Node(value)
                parent.right = newNode
                self.size += 1  # new node added, increment size
                return newNode
            else:
                return self._insert_recursive(parent.right, value)

    def search(self, value) -> bool:
        """
        TODO (Student):
        Search for a value in the BST.

        Requirements:
        - Return True if found.
        - Return False if not found.
        - Add comments explaining why BST search is often
          more efficient than linear search.
        """
        if self.root is None:
            return False
        else:
            return self._search_recursive(self.root, value)

    def _search_recursive(self, node: Node | None, value) -> bool:
        """
        TODO (Student):
        Implement recursive BST search.
        """
        # if we have navigated to a null node, it means the value was not found
        if node is None:
            return False

        # compare against node.value. If not found, continue recursively down the
        # appropriate tree path
        if node.value == value:
            return True
        elif value < node.value:
            return self._search_recursive(node.left, value)
        elif value > node.value:
            return self._search_recursive(node.right, value)

        # BST is faster than linear search because the search typically starts at a
        # midpoint of the list, and with each recursive search, a chunk of the search
        # based is removed from the search pool. This only works with a sorted tree
        return False

    def inorder(self):
        """
        TODO (Student):
        Return a list containing the values from an
        in-order traversal.
        """
        values = []
        if self.root is not None:
            # we pass a reference to the values list into the recursive
            # function, so no values will need to be returned. The list
            # of values will be updated through recursion
            self._inorder_recursive(self.root, values)
        return values

    def _inorder_recursive(self, node: Node | None, values):
        """
        TODO (Student):
        Implement in-order traversal.

        Requirements:
        - Visit the left subtree.
        - Visit the current node.
        - Visit the right subtree.
        - Add comments explaining why this traversal
          produces sorted output in a BST.
        """
        if node is None:
            return  # no value in a null node, so don't update values
        else:
            # progress down the left child nodes to the end, adding values lower than
            # the current node
            self._inorder_recursive(node.left, values)
            # add the current node
            values.append(node.value)
            # progress down the right child nodes to the end, adding values greater than
            # the current node
            self._inorder_recursive(node.right, values)


def main():
    print("=== UNIT 4: BINARY SEARCH TREES ===")

    # ===============================
    # TODO (Student): BUILD A TREE
    # ===============================
    #
    # Requirements:
    # 1. Create a BST object.
    # 2. Insert at least 7 values.
    # 3. Include values that go into both left
    #    and right subtrees.
    # 4. Display the values inserted.
    # 5. Use comments to explain why a BST is efficient at reducing search space for each step.

    print("\n=== TREE CONSTRUCTION ===")
    print("TODO: Create a BST and insert multiple values.")

    # create Binary Search Tree instance
    print("\nCreating BST...")
    bst = BST()

    insert_vals = [10, 4, 5, 18, 13, 14, 20]
    for val in insert_vals:
        bst.insert(val)

    # Runs the following commands in order:
    # bst.insert(10)      # root node is set to 10
    # bst.insert(4)       # left child of 10
    # bst.insert(5)       # right child of 4
    # bst.insert(18)      # right child of 10
    # bst.insert(13)      # left child of 18
    # bst.insert(14)      # right child of 13
    # bst.insert(20)      # right child of 18

    # BST looks like the tree below:
    #
    #     10
    #    /  \
    #   4    18
    #    \   / \
    #     5 13  20
    #        \
    #         14

    # display tree nodes in order
    print("Values were inserted in the following order")
    print("  \u2192 " + ", ".join([str(x) for x in bst.inorder()]))
    if bst.root:
        print(f"  \u2192 Root Node: {bst.root.value}")
        print(f"  \u2192 Count of Values in Tree: {bst.size}")

    # ===============================
    # TODO (Student): IN-ORDER TRAVERSAL
    # ===============================
    #
    # Requirements:
    # 1. Perform an in-order traversal.
    # 2. Display the traversal results.
    # 3. Use comments to explain why the traversal produces
    #    sorted output in a BST.

    print("\n=== IN-ORDER TRAVERSAL ===")
    print("TODO: Display and explain traversal results.")

    # The inorder() method visits the left child at each node recursively
    # (the lower number) before referencing its own value, then visiting
    # the nodes of the right child (greater numbers). In the example above,
    # this means the function does the following:
    #   * Visit 10 left child
    #     * Visit 4 left child (finds null)
    #     * Visit 4 and add to list                         4
    #     * Visit 4 right child
    #       * Visit 5 left child (finds null)
    #       * Visit 5 and add to list                       5
    #       * Visit 5 right child (finds null)
    #   * Visit 10 and add to list                         10
    #   * Visit 10 right child
    #     * Visit 18 left child
    #       * Visit 13 left child (finds null)
    #       * Visit 13 and add to list                     13
    #       * Visit 13 right child
    #         * Visit 14 left child (finds null)
    #         * Visit 14 and add to list                   14
    #         * Visit 14 left child (finds null)
    #     * Visit 18 and add to list                       18
    #     * Visit 18 right child
    #       * Visit 20 left child (finds null)
    #       * Visit 20 and add to list                     20
    #       * Visit 20 right child (finds null)
    #
    # Because the traversal visits left child at each node before visiting the node value, and
    # visits right child descendant nodes after visiting the node value, this results in a
    # sorted list.
    print("\nPrinting BST after in-order traversal:")
    print("  \u2192 " + ", ".join([str(x) for x in bst.inorder()]))

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for at least two values that exist.
    # 2. Search for at least two values that do not exist.
    # 3. Use comments to clearly explain the results.

    print("\n=== SEARCH TESTS ===")
    print("TODO: Demonstrate BST searching.")

    # First 2 values are in the tree, last 2 do not exist
    search_list = [14, 4, 200, 0]
    for search_val in search_list:
        print(f"\nSearching for {search_val} in the tree...")
        print(f"  \u2192 {search_val} found: {bst.search(search_val)}")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least one edge case.
    #
    # Example ideas:
    # - Traverse an empty tree
    # - Search an empty tree
    # - Insert duplicate values
    # - Create a tree with only one node
    #
    # Use comments to explain what happens and why.

    print("\n=== EDGE CASES ===")
    print("TODO: Demonstrate and explain an edge case.")

    print("\nCreating an empty BST...")
    bst_edge = BST()
    print(f"  \u2192 Root Node: {bst_edge.root}")
    print(f"  \u2192 Count of Values in Tree: {bst_edge.size}")

    print("\nAttempting Search on empty BST:")
    # In the initial search() method, when root is found to equal None, it immediately returns false
    print(f"  \u2192 Searching for 5 returns: {bst_edge.search(5)}")

    print("\nAttempting Traversal on empty BST:")
    # In the inorder() method, recursive inorder traversal only occurs if the root node is not None
    # If root is None, it immediately returns an empty list
    print(f"  \u2192 Traversing empty BST returns {bst_edge.inorder()}")

    # ===============================
    # TODO (Student): REAL WORLD SCENARIO
    # ===============================

    print("\n=== REAL WORLD SCENARIO ===")
    print("TODO: Demonstrate a real-world use case.")

    # binary search tree performance shines when the count of values being searched
    # grows very large. Databases such as Spotify's catalog of music may use something
    # like Binary Search to quicky find the artists or songs we search for. Searching
    # every record in order would prove to be a very slow operation
    print("\nCreating a sample of artists on Spotify:")
    spotify_catalog = BST()

    artists = [
        "noah kahan",
        "needtobreathe",
        "twenty one pilots",
        "two friends",
        "noah cyrus",
        "two door cinema",
        "wolves at the gate",
        "mayday parade",
    ]
    for artist in artists:
        spotify_catalog.insert(artist)

    print("  \u2192 " + ", ".join([str(x) for x in spotify_catalog.inorder()]))
    print("\nSearching for Twenty One Pilots:")
    print(f"  \u2192 Returns: {spotify_catalog.search('Twenty One Pilots'.lower())}")

    print("\nAdding new artist to catalog:")
    new = spotify_catalog.insert("memphis may fire")
    if new:
        print(f"  \u2192 Added: {new.value.title()}")
        print(
            "  \u2192 Current Artist List: \n    \u2192 "
            + "\n    \u2192 ".join([str(x).title() for x in spotify_catalog.inorder()])
        )


if __name__ == "__main__":
    main()
