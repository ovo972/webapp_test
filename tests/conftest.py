import os
import sys
import pytest

# S'assurer que l'import fonctionne quel que soit le dossier depuis lequel pytest est lancé
THIS_DIR = os.path.dirname(__file__)
PROJECT_ROOT = os.path.abspath(os.path.join(THIS_DIR, ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

try:
    # On s'attend à une app Quart située dans api/sample_api.py
    from api.sample_api import app
except Exception as exc:
    raise RuntimeError(f"Impossible d'importer 'app' depuis api.sample_api: {exc}") from exc


@pytest.fixture
def test_client():
    # Pour Quart: client async utilisable avec "async with" et await response.get_json()
    return app.test_client()