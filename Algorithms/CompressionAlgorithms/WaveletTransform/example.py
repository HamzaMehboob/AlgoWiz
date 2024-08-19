import numpy as np
from wavelet_transform import haar_wavelet_transform, inverse_haar_wavelet_transform

# Example matrix
matrix = np.array([
    [4, 6, 10, 12],
    [14, 16, 18, 20],
    [24, 26, 30, 32],
    [34, 36, 38, 40]
], dtype=float)

# Perform Haar wavelet transform
transformed = haar_wavelet_transform(matrix)
print("Transformed Matrix:")
print(transformed)

# Perform inverse Haar wavelet transform
inverse_transformed = inverse_haar_wavelet_transform(transformed)
print("\nInverse Transformed Matrix:")
print(inverse_transformed)

# Verify correctness
assert np.allclose(matrix, inverse_transformed), "Wavelet transform and inverse transform failed."
print("Wavelet transform and inverse transform successful.")
