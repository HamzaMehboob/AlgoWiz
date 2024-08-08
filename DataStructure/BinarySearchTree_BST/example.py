from bst import BinarySearchTree

def main():
    # Create a Binary Search Tree
    bst = BinarySearchTree()

    # Insert elements
    bst.insert(50)
    bst.insert(30)
    bst.insert(20)
    bst.insert(40)
    bst.insert(70)
    bst.insert(60)
    bst.insert(80)

    # Search for an element
    key = 40
    if bst.search(key):
        print(f"Element {key} found in the BST.")
    else:
        print(f"Element {key} not found in the BST.")

    # Print inorder traversal
    print("Inorder traversal of the BST:", bst.inorder())

if __name__ == "__main__":
    main()
