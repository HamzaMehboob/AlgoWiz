# Boyer-Moore String Search Algorithm

The Boyer-Moore algorithm is an efficient string searching algorithm that skips sections of the text to speed up the search process. This repository contains a Python implementation of the Boyer-Moore algorithm for substring search.

## Files

- `boyer_moore.py`: Contains the implementation of the Boyer-Moore algorithm.
- `example.py`: Provides an example of how to use the Boyer-Moore class to search for a pattern in a text.

## How to Use

1. Clone the repository or download the files.
2. Ensure you have Python installed on your machine.
3. Run `example.py` to see the Boyer-Moore algorithm in action:

    ```bash
    python example.py
    ```

4. The output will show the index at which the pattern was found in the given text.

## Example

In the provided `example.py`, the algorithm searches for the pattern `"ABCD"` in the text `"ABAAABCDABABCDABCDABDE"`. The output should be:

