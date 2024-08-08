from trie import Trie

def main():
    # Create a Trie instance
    trie = Trie()

    # Insert words into the Trie
    trie.insert("apple")
    trie.insert("app")
    trie.insert("banana")

    # Search for words
    print("Searching for 'app':", trie.search("app"))      # True
    print("Searching for 'apple':", trie.search("apple"))  # True
    print("Searching for 'banana':", trie.search("banana")) # True
    print("Searching for 'ban':", trie.search("ban"))      # False

    # Check if any words start with a given prefix
    print("Starts with 'app':", trie.starts_with("app"))   # True
    print("Starts with 'ban':", trie.starts_with("ban"))   # True
    print("Starts with 'bana':", trie.starts_with("bana"))  # True
    print("Starts with 'bat':", trie.starts_with("bat"))   # False

if __name__ == "__main__":
    main()
