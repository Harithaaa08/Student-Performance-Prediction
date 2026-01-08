import joblib
from data.load_data import load_data
from data.preprocess_data import preprocess_data
from model.train_model import train_model

def train_save():
    df = load_data()

    X_train, X_test, y_train, y_test = preprocess_data(df)

    model = train_model(X_train, y_train, X_test, y_test)

    joblib.dump(model, "student_performance_model.pkl")
    print("✅ Model saved as student_performance_model.pkl")

if __name__ == "__main__":
    train_save()
