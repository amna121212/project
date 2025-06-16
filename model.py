from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris

 
class SVMModel:
    def __init__(self, kernel='linear'):
        self.kernel = kernel
        self.model = SVC(kernel=self.kernel)

    def train(self, X, y):
        """Splits data and trains the SVM model."""
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        self.model.fit(X_train, y_train)
        print("Model training complete.")
        return X_test, y_test

    def predict(self, X_test):
        return self.model.predict(X_test)

# ✅ Example usage
if __name__ == "__main__":
    iris = load_iris()
    X, y = iris.data, iris.target

    model = SVMModel(kernel='linear')
    X_test, y_test = model.train(X, y)
    preds = model.predict(X_test)

    print("Predictions:", preds)

