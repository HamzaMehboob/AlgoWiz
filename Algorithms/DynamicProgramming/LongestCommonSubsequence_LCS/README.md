# Longest Common Subsequence (LCS) Algorithm

This repository contains an implementation of the Longest Common Subsequence (LCS) algorithm in Python. The LCS problem is a classic computer science problem used to find the longest subsequence that is common to two sequences.

## Introduction

The Longest Common Subsequence problem is used in various fields including computational biology, version control systems, and text comparison. This implementation provides a method to compute both the length and the actual subsequence.

## Features

- Computes the length of the LCS for two input sequences.
- Retrieves the actual LCS sequence.
- Handles general cases of sequences.

## Requirements

- Python 3.x

## Usage

1. Clone the repository:
    ```sh
    git clone https://github.com/HamzaMehboob/AlgoWiz.git
    cd AlgoWiz/Algorithms/DynamicProgramming/LongestCommonSubsequence_LCS
    ```

2. Run the example script:
    ```sh
    python example.py
    ```

## Example

Here is an example usage of the LCS algorithm:

```python
from lcs import LCS

x = "AGGTAB"
y = "GXTXAYB"
lcs = LCS(x, y)

print(f"LCS Length: {lcs.compute_lcs()}")
print(f"LCS Sequence: {lcs.get_lcs()}")

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact me

If you have any query, ask me at hamzamehboob103@gmail.com