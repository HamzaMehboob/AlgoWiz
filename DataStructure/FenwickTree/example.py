from fenwick_tree import FenwickTree

def main():
    # Initialize Fenwick Tree with size 10
    size = 10
    fenwick_tree = FenwickTree(size)

    # Update values
    fenwick_tree.update(1, 5)
    fenwick_tree.update(3, 2)
    fenwick_tree.update(5, 8)

    # Query prefix sums
    print("Prefix sum up to index 5:", fenwick_tree.query(5))  # Output: 15

    # Query range sum
    print("Range sum from index 2 to 5:", fenwick_tree.range_query(2, 5))  # Output: 10

if __name__ == "__main__":
    main()
