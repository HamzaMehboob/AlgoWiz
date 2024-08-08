
from decision_tree import DecisionTreeModel
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# Load sample dataset
iris = load_iris()
X = iris.data
y = iris.target

# Split dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Initialize and train the decision tree model
dt_model = DecisionTreeModel(criterion='entropy', max_depth=3)
dt_model.train(X_train, y_train)

# Evaluate the model
accuracy = dt_model.score(X_test, y_test)
print(f"Accuracy of Decision Tree Classifier: {accuracy:.2f}")
