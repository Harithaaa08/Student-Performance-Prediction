from backend.data.load_data import load_data
from backend.data.preprocess_data import preprocess_data
from backend.model.train_model import train_model


def test_train_model_predicts():
    df = load_data()
    X_train, X_test, y_train, y_test = preprocess_data(df)
    model = train_model(X_train, y_train, X_test, y_test)
    preds = model.predict(X_test.iloc[:5])
    assert len(preds) == 5
