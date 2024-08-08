from red_black_tree import RedBlackTree

def example_red_black_tree():
    print("Red-Black Tree:")
    rbt = RedBlackTree()
    rbt.insert(10)
    rbt.insert(20)
    rbt.insert(30)
    rbt.insert(15)
    rbt.insert(25)
    rbt.print_tree()

def main():
    example_red_black_tree()

if __name__ == "__main__":
    main()
