from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

class Evaluator:
    def __init__(self, y_test, y_pred):
        self.y_test = y_test
        self.y_pred = y_pred

    def evaluate(self):
        print("Evaluation Results:")
        print(confusion_matrix(self.y_test, self.y_pred))
        print(classification_report(self.y_test, self.y_pred))
        print("Accuracy:", accuracy_score(self.y_test, self.y_pred))


 
y_test = [0, 1, 1, 0, 1]
y_pred = [0, 1, 0, 0, 1]

 
evaluator = Evaluator(y_test, y_pred)
 
evaluator.evaluate()

