from avl_tree import AVLTree

def main():
    # Create an AVL Tree
    avl = AVLTree()
    root = None

    # Insert elements
    elements = [20, 30, 10, 5, 3, 4, 15]
    for el in elements:
        root = avl.insert(root, el)

    # Print inorder traversal
    print("Inorder traversal of the AVL tree:", avl.inorder(root))

if __name__ == "__main__":
    main()
