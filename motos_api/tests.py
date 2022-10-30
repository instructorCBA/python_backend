from django.test import TestCase
from .models import Moto

# Create your tests here.
class MotoModelTest(TestCase):
     @classmethod
     
     def setUpTestData(cls):
          cls.moto = Moto.objects.create(
               reference="prueba",
               trademark="marca prueba",
               model="año prueba",
               price=20000,
               image="imagen prueba",
               supplier="proveedor prueba"
          )
          
     def test_model_content (self):
          self.assertEqual(self.moto.reference, "prueba")
          self.assertEqual(self.moto.trademark, "marca prueba")
          self.assertEqual(self.moto.model, "año prueba")
          self.assertEqual(self.moto.price, 20000)
          self.assertEqual(self.moto.image, "imagen prueba")
          self.assertEqual(self.moto.supplier, "proveedor prueba")
          self.assertEqual(str(self.moto), "prueba")