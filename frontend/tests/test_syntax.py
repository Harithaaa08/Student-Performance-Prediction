import py_compile


def test_frontend_compiles():
    # Ensure the Streamlit app has no syntax errors
    py_compile.compile("frontend/app.py", doraise=True)
