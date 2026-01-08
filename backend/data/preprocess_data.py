from sklearn.model_selection import train_test_split

def preprocess_data(df):
    # Convert Yes/No → 1/0
    df['Extracurricular Activities'] = df['Extracurricular Activities'].map({
        'Yes': 1,
        'No': 0
    })

    X = df.drop('Performance Index', axis=1)
    y = df['Performance Index']

    return train_test_split(
        X, y,
        test_size=0.2,
        random_state=42
    )
