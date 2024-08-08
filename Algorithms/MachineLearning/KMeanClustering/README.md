# K-Means Clustering

This repository contains a simple implementation of the K-Means clustering algorithm using the `scikit-learn` library in Python. The K-Means algorithm is a popular unsupervised learning algorithm used to partition a dataset into clusters.

## Introduction

K-Means clustering partitions data into `k` clusters where each data point belongs to the cluster with the nearest mean. The algorithm is iterative and aims to minimize the variance within each cluster.

## Features

- Implementation of K-Means clustering using `scikit-learn`.
- Example code to train and evaluate the model using the Iris dataset.
- Visualization of clusters in 2D space.

## Requirements

- Python 3.x
- `scikit-learn` library (install via `pip install scikit-learn`)
- `matplotlib` library (install via `pip install matplotlib`)

## Usage

1. Clone the repository:
    ```sh
    git clone https://github.com/HamzaMehboob/AlgoWiz.git
    cd AlgoWiz/Algorithms/MachineLearning/KMeanClustering
    ```

2. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

3. Run the example script:
    ```sh
    python example.py
    ```

## Example

Here is an example usage of the K-Means Clustering implementation:

```python
from kmeans_clustering import KMeansClustering
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# Load sample dataset
iris = load_iris()
X = iris.data[:, :2]  # Only take the first two features for 2D plotting
y = iris.target

# Split dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Initialize and train the K-Means model
kmeans = KMeansClustering(n_clusters=3)
kmeans.fit(X_train)

# Predict and plot the results
kmeans.plot_clusters(X_test, y_test)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact me

If you have any query, ask me at hamzamehboob103@gmail.com