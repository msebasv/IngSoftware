from django.test import TestCase
from django.contrib.auth.models import User
from user.forms import CustomUserCreationForm, FormLogin

class FormTestCase(TestCase):
    def test_custom_user_creation_form(self):
        # Crea datos de prueba para el formulario
        form_data = {
            'username': 'testuser',
            'password1': 'testpassword',
            'password2': 'testpassword',
        }

        # Crea una instancia del formulario con los datos de prueba
        form = CustomUserCreationForm(data=form_data)

        # Verifica que el formulario sea válido
        self.assertTrue(form.is_valid())

        # Guarda el usuario creado por el formulario
        user = form.save()

        # Verifica que el usuario se haya guardado correctamente
        self.assertEqual(User.objects.count(), 1)
        saved_user = User.objects.first()
        self.assertEqual(saved_user.username, 'testuser')

        # Verifica que la contraseña se haya encriptado correctamente
        self.assertNotEqual(saved_user.password, 'testpassword')

    def test_form_login(self):
        # Crea datos de prueba para el formulario
        form_data = {
            'username': 'testuser',
            'password': 'testpassword',
        }

        # Crea una instancia del formulario con los datos de prueba
        form = FormLogin(data=form_data)

        # Verifica que el formulario sea válido
        self.assertTrue(form.is_valid())

        # Verifica que los atributos del campo username se hayan configurado correctamente
        self.assertEqual(form.fields['username'].widget.attrs['class'], 'form-control')
        self.assertEqual(form.fields['username'].widget.attrs['placeholder'], 'Usuario')

        # Verifica que los atributos del campo password se hayan configurado correctamente
        self.assertEqual(form.fields['password'].widget.attrs['class'], 'form-control')
        self.assertEqual(form.fields['password'].widget.attrs['placeholder'], 'Contraseña')
