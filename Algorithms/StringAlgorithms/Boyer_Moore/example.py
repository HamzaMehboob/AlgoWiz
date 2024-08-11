# example.py

from boyer_moore import BoyerMoore

def main():
    text = "ABAAABCDABABCDABCDABDE"
    pattern = "ABCD"
    
    bm = BoyerMoore(pattern)
    index = bm.search(text)
    
    if index != -1:
        print(f"Pattern found at index: {index}")
    else:
        print("Pattern not found")

if __name__ == "__main__":
    main()
