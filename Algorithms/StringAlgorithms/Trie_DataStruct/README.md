# Trie Data Structure

A Trie (pronounced "try") is a tree-like data structure used to efficiently store and search a dynamic set of strings. It is often used for tasks such as autocomplete and spell checking.

## Features

- **Insert**: Add a word to the trie.
- **Search**: Check if a word exists in the trie.
- **Starts With**: Check if there is any word in the trie that starts with a given prefix.

## Installation

No additional libraries are required. This implementation uses only Python's built-in features.

## Usage

1. Clone the repository or download the files.
2. Run the `example.py` script to see the Trie data structure in action.

### Example

```python
from trie import Trie

def main():
    trie = Trie()
    trie.insert("apple")
    trie.insert("app")
    trie.insert("banana")

    print("Searching for 'app':", trie.search("app"))      # True
    print("Searching for 'apple':", trie.search("apple"))  # True
    print("Searching for 'banana':", trie.search("banana")) # True
    print("Searching for 'ban':", trie.search("ban"))      # False

    print("Starts with 'app':", trie.starts_with("app"))   # True
    print("Starts with 'ban':", trie.starts_with("ban"))   # True
    print("Starts with 'bana':", trie.starts_with("bana"))  # True
    print("Starts with 'bat':", trie.starts_with("bat"))   # False

if __name__ == "__main__":
    main()

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact me

If you have any query, ask me at hamzamehboob103@gmail.com