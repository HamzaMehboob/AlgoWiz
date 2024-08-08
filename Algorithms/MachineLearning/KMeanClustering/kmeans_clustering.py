from sklearn.cluster import KMeans
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

class KMeansClustering:
    def __init__(self, n_clusters=3, random_state=42):
        self.n_clusters = n_clusters
        self.random_state = random_state
        self.model = KMeans(n_clusters=self.n_clusters, random_state=self.random_state)
    
    def fit(self, X_train):
        self.model.fit(X_train)
    
    def predict(self, X_test):
        return self.model.predict(X_test)
    
    def plot_clusters(self, X, y=None):
        # Ensure `X` is a 2D array
        if X.ndim != 2 or X.shape[1] != 2:
            raise ValueError("X should be a 2D array with 2 features for plotting")

        # If y is provided, use it for color coding; otherwise, use model labels
        if y is not None:
            plt.scatter(X[:, 0], X[:, 1], c=y, cmap='viridis', marker='o', edgecolor='k')
        else:
            if len(self.model.labels_) != X.shape[0]:
                raise ValueError("Size of `self.model.labels_` does not match the size of `X`")
            plt.scatter(X[:, 0], X[:, 1], c=self.model.labels_, cmap='viridis', marker='o', edgecolor='k')

        plt.xlabel('Feature 1')
        plt.ylabel('Feature 2')
        plt.title('K-Means Clustering')
        plt.colorbar(label='Cluster')
        plt.show()


if __name__ == "__main__":
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
