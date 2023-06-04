from django.test import TestCase
from django.core.exceptions import ValidationError
from administrator.models import Administrative, Committee, ActType, Act

class ModelTestCase(TestCase):
    def test_administrative_model(self):
        # Crea una instancia del modelo Administrative
        administrative = Administrative(salary=5000.0, position='Manager')

        # Verifica que se pueda guardar correctamente
        administrative.save()
        self.assertEqual(Administrative.objects.count(), 1)

        # Verifica que los atributos se hayan guardado correctamente
        saved_administrative = Administrative.objects.first()
        self.assertEqual(saved_administrative.salary, 5000.0)
        self.assertEqual(saved_administrative.position, 'Manager')

        # Verifica que el atributo user_id sea requerido
        administrative.user_id = None
        with self.assertRaises(ValidationError):
            administrative.full_clean()

    def test_committee_model(self):
        # Crea una instancia del modelo Committee
        committee = Committee(name='Committee 1')

        # Verifica que se pueda guardar correctamente
        committee.save()
        self.assertEqual(Committee.objects.count(), 1)

        # Verifica que el método __str__ devuelva el nombre correcto
        self.assertEqual(str(committee), 'Committee 1')

    # Agrega pruebas para los demás modelos (ActType, Act)