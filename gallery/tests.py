from django.test import TestCase
from gallery.models import Category, Image
from django.utils import timezone
from datetime import date
from django.core.files.uploadedfile import SimpleUploadedFile


class CategoryModelTest(TestCase):
    def test_create_category(self):
        category = Category.objects.create(name="Test")
        self.assertEqual(category.name, "Test")
        self.assertTrue(isinstance(category, Category))
        self.assertEqual(category.__str__(), category.name)

