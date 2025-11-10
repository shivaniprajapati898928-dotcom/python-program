# Using Scikit-learn, load a sample dataset (e.g., Iris), split it into training and testing sets, train a simple Logistic Regression model, and report accuracy

# Import necessary libraries
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Step 1: Load the Iris dataset
iris = load_iris()
X = iris.data        # Features (sepal length, width, etc.)
y = iris.target      # Target (species)

print("Iris dataset loaded successfully!")
print(f"Feature shape: {X.shape}")
print(f"Target shape: {y.shape}")

# Step 2: Split into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("\nDataset split into training and testing sets.")
print(f"Training size: {len(X_train)} | Testing size: {len(X_test)}")

# Step 3: Train Logistic Regression model
model = LogisticRegression(max_iter=200)  # Increase iterations for convergence
model.fit(X_train, y_train)

print("\nLogistic Regression model trained successfully!")

# Step 4: Make predictions
y_pred = model.predict(X_test)

# Step 5: Evaluate accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"\n🎯 Model Accuracy on Test Data: {accuracy * 100:.2f}%")

# Optional: Display sample predictions
print("\nSample Predictions:")
for i in range(5):
    print(f"Actual: {y_test[i]}, Predicted: {y_pred[i]}")
