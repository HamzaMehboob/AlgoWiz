import numpy as np

def haar_wavelet_transform(matrix):
    """Perform a Haar wavelet transform on a 2D matrix."""
    def haar_1d(arr):
        n = len(arr)
        output = np.zeros(n)
        while n > 1:
            n = n // 2
            avg = (arr[0:2*n:2] + arr[1:2*n:2]) / 2
            diff = (arr[0:2*n:2] - arr[1:2*n:2]) / 2
            output[0:n] = avg
            output[n:2*n] = diff
            arr = output.copy()
        return output
    
    rows, cols = matrix.shape
    transformed = np.zeros((rows, cols))
    
    # Apply Haar transform on rows
    for i in range(rows):
        transformed[i, :] = haar_1d(matrix[i, :])
    
    # Apply Haar transform on columns
    for j in range(cols):
        transformed[:, j] = haar_1d(transformed[:, j])
    
    return transformed

def inverse_haar_wavelet_transform(matrix):
    """Perform an inverse Haar wavelet transform on a 2D matrix."""
    def inverse_haar_1d(arr):
        n = len(arr)
        output = np.zeros(n)
        while n < len(arr):
            n = n * 2
            avg = arr[0:n//2]
            diff = arr[n//2:n]
            output[0:2*n:2] = avg + diff
            output[1:2*n:2] = avg - diff
        return output
    
    rows, cols = matrix.shape
    transformed = np.zeros((rows, cols))
    
    # Apply inverse Haar transform on columns
    for j in range(cols):
        transformed[:, j] = inverse_haar_1d(matrix[:, j])
    
    # Apply inverse Haar transform on rows
    for i in range(rows):
        transformed[i, :] = inverse_haar_1d(transformed[i, :])
    
    return transformed

# Example Usage
if __name__ == "__main__":
    matrix = np.array([
        [4, 6, 10, 12],
        [14, 16, 18, 20],
        [24, 26, 30, 32],
        [34, 36, 38, 40]
    ], dtype=float)

    print("Original Matrix:")
    print(matrix)

    transformed = haar_wavelet_transform(matrix)
    print("\nTransformed Matrix:")
    print(transformed)

    inverse_transformed = inverse_haar_wavelet_transform(transformed)
    print("\nInverse Transformed Matrix:")
    print(inverse_transformed)
