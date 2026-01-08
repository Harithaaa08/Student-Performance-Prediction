from load_data import load_data
from preprocess_data import preprocess_data

df = load_data()
X_train, X_test, y_train, y_test = preprocess_data(df)

print("X_train shape:", X_train.shape)
print("X_test shape:", X_test.shape)
