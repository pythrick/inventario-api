import pytest

from inventario.models import Usuario


@pytest.mark.django_db
class TestUsuarioManager:
    def test_create_user(self, fake):
        name = fake.name()
        email = fake.email()
        password = fake.password(
            length=10, special_chars=True, digits=True, upper_case=True, lower_case=True
        )
        usuario = Usuario.objects.create_user(name=name, email=email, password=password)

        assert usuario.name == name, f"O nome do usuário deve ser: {name}"
        assert usuario.email == email, f"O e-mail do usuário deve ser: {email}"
        assert usuario.password, "A senha deve ter sido gravada."
        assert (
            usuario.password != password
        ), f"A senha do usuário não deve ser a mesma que a informada."
        assert usuario.check_password(
            password
        ), f"A senha não foi encodada/gravada corretamente."

    def test_create_super_user(self, fake):
        name = fake.name()
        email = fake.email()
        password = fake.password(
            length=10, special_chars=True, digits=True, upper_case=True, lower_case=True
        )
        usuario = Usuario.objects.create_superuser(
            name=name, email=email, password=password
        )

        assert usuario.is_staff, "O super usuário deve ser membro do time."
        assert usuario.is_active, "O super usuário deve estar ativo."
        assert usuario.is_superuser, "O super usuário deve ser um super usuário."
