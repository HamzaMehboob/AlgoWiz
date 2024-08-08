from kmp import KMP

def main():
    # Define the pattern and the text
    pattern = "abc"
    text = "abcpqrabcxyzabc"

    # Create a KMP instance
    kmp = KMP(pattern)

    # Search for the pattern in the text
    indices = kmp.search(text)

    # Print the results
    print(f"Pattern '{pattern}' found at indices: {indices}")

if __name__ == "__main__":
    main()
