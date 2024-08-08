from rabin_karp import RabinKarp

def main():
    # Define the pattern and the text
    pattern = "test"
    text = "This is a test text for testing the Rabin-Karp algorithm."

    # Create a Rabin-Karp instance
    rk = RabinKarp(pattern)

    # Search for the pattern in the text
    indices = rk.search(text)

    # Print the results
    print(f"Pattern '{pattern}' found at indices: {indices}")

if __name__ == "__main__":
    main()
