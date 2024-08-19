# Wavelet Transform (Haar) for JPEG 2000

## Overview

This project demonstrates a basic implementation of the Haar wavelet transform, which is a fundamental wavelet transform used in image compression techniques such as JPEG 2000. The Haar transform is used to simplify and compress image data by transforming it into a different domain.

## Files

- **wavelet_transform.py**: Contains the implementation of the Haar wavelet transform and its inverse.
- **example.py**: Demonstrates how to use the Haar wavelet transform functions with example data.
- **README.md**: Provides documentation for the wavelet transform.

## Haar Wavelet Transform

### `haar_wavelet_transform(matrix)`

Performs a Haar wavelet transform on a 2D matrix. The function applies the Haar wavelet transform first on the rows and then on the columns.

### `inverse_haar_wavelet_transform(matrix)`

Performs an inverse Haar wavelet transform on a 2D matrix to reconstruct the original matrix.

## Usage

### Transforming Data

To perform the Haar wavelet transform on a matrix:

```python
from wavelet_transform import haar_wavelet_transform

matrix = np.array([
    [4, 6, 10, 12],
    [14, 16, 18, 20],
    [24, 26, 30, 32],
    [34, 36, 38, 40]
], dtype=float)

transformed = haar_wavelet_transform(matrix)
print("Transformed Matrix:")
print(transformed)
