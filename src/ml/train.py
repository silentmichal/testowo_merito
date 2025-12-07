from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import joblib

def train():
    data = load_iris()
    clf = RandomForestClassifier()
    clf.fit(data.data, data.target)
    joblib.dump(clf, "src/ml/model.pkl")
    print("Model zapisany jako model.pkl")

if __name__ == "__main__":
    train()
