import importlib, os, sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def test_import():
    assert importlib.import_module('location_sampler')
