from backend.data.load_data import load_data


def test_load_data():
    df = load_data()
    assert not df.empty
    assert 'Hours Studied' in df.columns
    assert df.shape[1] == 6
