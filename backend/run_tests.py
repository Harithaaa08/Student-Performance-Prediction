import importlib
import traceback
import sys
from pathlib import Path

# Ensure project root is on sys.path so imports like `backend.*` work
project_root = Path(__file__).resolve().parents[1]
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

TEST_MODULES = [
    "backend.tests.test_load",
    "backend.tests.test_preprocess",
    "backend.tests.test_train_model",
    "backend.tests.test_api",
    "frontend.tests.test_syntax",
]

if __name__ == "__main__":
    failures = []
    for mod_name in TEST_MODULES:
        print(f"Running tests in {mod_name}...")
        try:
            mod = importlib.import_module(mod_name)
        except Exception:
            print(f"Failed to import {mod_name}")
            traceback.print_exc()
            failures.append(mod_name)
            continue

        for name in dir(mod):
            if name.startswith("test_"):
                func = getattr(mod, name)
                try:
                    func()
                    print(f"  ✅ {name}")
                except Exception:
                    print(f"  ❌ {name}")
                    traceback.print_exc()
                    failures.append(f"{mod_name}.{name}")

    print("\nTest run complete.")
    if failures:
        print("Failures:")
        for f in failures:
            print(" - ", f)
        raise SystemExit(1)
    else:
        print("All tests passed ✅")
