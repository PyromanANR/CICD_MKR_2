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


class ImageModelTest(TestCase):
    def setUp(self):
        self.category1 = Category.objects.create(name="Test1")
        self.category2 = Category.objects.create(name="Test2")

    def test_create_image(self):
        image = Image.objects.create(
            title="Sunset",
            image=SimpleUploadedFile(name='test_image.jpg', content=b'', content_type='image/jpeg'),
            created_date=date.today(),
            age_limit=18
        )
        image.categories.add(self.category1, self.category2)
        image.save()

        self.assertEqual(image.title, "Sunset")
        self.assertTrue(isinstance(image, Image))
        self.assertEqual(image.__str__(), image.title)
        self.assertEqual(image.age_limit, 18)
        self.assertEqual(image.created_date, date.today())
        self.assertIn(self.category1, image.categories.all())
        self.assertIn(self.category2, image.categories.all())

    def test_image_category(self):
        image = Image.objects.create(
            title="Category_test",
            image=SimpleUploadedFile(name='test_image.jpg', content=b'', content_type='image/jpeg'),
            created_date=date.today(),
            age_limit=12
        )
        image.categories.add(self.category2)
        image.save()

        self.assertEqual(image.categories.count(), 1)
        self.assertIn(self.category2, image.categories.all())
        self.assertNotIn(self.category1, image.categories.all())