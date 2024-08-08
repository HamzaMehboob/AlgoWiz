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
