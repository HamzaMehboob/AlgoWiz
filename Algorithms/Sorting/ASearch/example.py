# example.py

from interpolation_search import InterpolationSearch

def main():
    data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    target = 70
    
    searcher = InterpolationSearch(data)
    index = searcher.search(target)
    
    if index != -1:
        print(f"Target found at index: {index}")
    else:
        print("Target not found")

if __name__ == "__main__":
    main()
