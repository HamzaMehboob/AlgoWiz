from segment_tree import SegmentTree

def example_segment_tree():
    data = [1, 3, 5, 7, 9, 11]
    seg_tree = SegmentTree(data)
    
    print("Initial Segment Tree:")
    print(f"Sum of values in range [1, 3]: {seg_tree.query(1, 3)}")
    
    seg_tree.update(1, 10)
    print("\nAfter updating index 1 to 10:")
    print(f"Sum of values in range [1, 3]: {seg_tree.query(1, 3)}")

def main():
    example_segment_tree()

if __name__ == "__main__":
    main()
