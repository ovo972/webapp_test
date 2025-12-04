import os
import sys
import pytest

# S'assurer que l'import fonctionne quel que soit le dossier depuis lequel pytest est lancé
THIS_DIR = os.path.dirname(__file__)
PROJECT_ROOT = os.path.abspath(os.path.join(THIS_DIR, ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)


@pytest.fixture
def test_client():
    """Retourne un client de test pour l'app Quart.

    Si une dépendance manquante (ex: asyncpg) empêche l'import de l'app,
    on skippe proprement les tests avec un message explicite.
    """
    try:
        from api.sample_api import app  # import paresseux pour gérer les erreurs proprement
    except ModuleNotFoundError as e:
        # Cas typique: ModuleNotFoundError: No module named 'asyncpg'
        if getattr(e, "name", "") == "asyncpg":
            pytest.skip(
                "Dépendance 'asyncpg' manquante. Installez les dépendances de l'API (api/requirements.txt) dans la CI."
            )
        raise
    except Exception as exc:
        raise RuntimeError(
            f"Impossible d'importer 'app' depuis api.sample_api: {exc}"
        ) from exc

    # Pour Quart: client async utilisable avec "async with" et await response.get_json()
    return app.test_client()