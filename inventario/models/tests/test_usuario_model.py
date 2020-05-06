import uuid

import pytest
from mixer.backend.django import mixer


@pytest.mark.django_db
class TestUsuarioModel:
    @pytest.fixture
    def usuario(self):
        return mixer.blend("inventario.Usuario")

    def test_pk(self, usuario):
        assert isinstance(
            usuario.pk, uuid.UUID
        ), f"A pk da {usuario.__class__.name} deveria ser um campo do tipo UUID."

    def test_string(self, usuario):
        assert (
            str(usuario) == usuario.name
        ), f"A string de {usuario.__class__.name} deveria ser o valor do campo name."
