from backend.data.load_data import load_data
from backend.data.preprocess_data import preprocess_data


def test_preprocess():
    df = load_data()
    X_train, X_test, y_train, y_test = preprocess_data(df)

    # five input features
    assert X_train.shape[1] == 5
    assert X_train.shape[0] > 0
    assert len(y_train) == X_train.shape[0]
    # Ensure extracurricular column present
    assert 'Extracurricular Activities' in X_train.columns
