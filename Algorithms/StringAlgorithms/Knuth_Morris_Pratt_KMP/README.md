# Knuth-Morris-Pratt (KMP) Algorithm

The Knuth-Morris-Pratt (KMP) algorithm is an efficient string matching algorithm that searches for occurrences of a "pattern" within a "text". It preprocesses the pattern to create a Longest Prefix Suffix (LPS) array which is used to skip unnecessary comparisons in the text.

## Features

- Efficient pattern matching
- Preprocesses the pattern to build an LPS array
- Avoids unnecessary comparisons by using the LPS array

## Installation

No additional libraries are required. This implementation uses only Python's built-in features.

## Usage

1. Clone this repository:

    ```bash
    git clone https://github.com/HamzaMehboob/AlgoWiz.git
    cd AlgoWiz/Algorithms/StringAlgorithms/Knuth_Morris_Pratt_KMP
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the example script:

    ```bash
    python example.py
    ```

### Example

```python
from kmp import KMP

def main():
    pattern = "abc"
    text = "abcpqrabcxyzabc"
    kmp = KMP(pattern)
    indices = kmp.search(text)
    print(f"Pattern '{pattern}' found at indices: {indices}")

if __name__ == "__main__":
    main()
## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact me

If you have any query, ask me at hamzamehboob103@gmail.com