# Decision Tree Classifier

This repository contains a simple implementation of a Decision Tree Classifier using the `scikit-learn` library in Python. The Decision Tree is a supervised learning algorithm used for classification and regression tasks.

## Introduction

A Decision Tree is a flowchart-like tree structure where each internal node represents a feature (or attribute), each branch represents a decision rule, and each leaf node represents an outcome. The path from the root to a leaf represents classification rules.

## Features

- Implementation of a Decision Tree Classifier using `scikit-learn`.
- Example code to train and evaluate the model using the Iris dataset.
- Customizable hyperparameters like `criterion` and `max_depth`.

## Requirements

- Python 3.x
- `scikit-learn` library (install via `pip install scikit-learn`)

## Usage

1. Clone the repository:
    ```sh
    git clone https://github.com/HamzaMehboob/AlgoWiz.git
    cd AlgoWiz/Algorithms/MachineLearning/DecisionTree
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

Here is an example usage of the Decision Tree Classifier:

```python
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

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact me

If you have any query, ask me at hamzamehboob103@gmail.com