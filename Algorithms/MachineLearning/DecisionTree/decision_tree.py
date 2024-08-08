from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

class DecisionTreeModel:
    def __init__(self, criterion='gini', max_depth=None):
        self.criterion = criterion
        self.max_depth = max_depth
        self.model = DecisionTreeClassifier(criterion=self.criterion, max_depth=self.max_depth)
    
    def train(self, X_train, y_train):
        self.model.fit(X_train, y_train)
    
    def predict(self, X_test):
        return self.model.predict(X_test)
    
    def score(self, X_test, y_test):
        y_pred = self.predict(X_test)
        return accuracy_score(y_test, y_pred)

if __name__ == "__main__":
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
