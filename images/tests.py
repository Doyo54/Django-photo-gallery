from unicodedata import category
from django.test import TestCase
from .models import Image, Category, Location


class TestImage(TestCase):
    def setUp(self):
        self.location = Location(location='Nairobi')
        self.location.save_location()

        self.category = Category(category='Travel')
        self.category.save_category()

        self.image_test = Image(id=1, name='food', description='this is a test image', location=self.location,
                                category=self.category)

    def test_instance(self):
        self.assertTrue(isinstance(self.image_test, Image))

    def test_save_image(self):
        self.image_test.save_image()
        after = Image.objects.all()
        self.assertTrue(len(after) > 0)

    def test_delete_image(self):
        self.image_test.delete_image()
        images = Image.objects.all()
        self.assertTrue(len(images) == 0)

    def test_update_image(self):
        self.image_test.save_image()
        self.image_test.update_image(self.image_test.id, 'image/test.jpg')
        changed_img = Image.objects.filter(image='image/test.jpg')
        self.assertTrue(len(changed_img) > 0)

    def tearDown(self):
        Image.objects.all().delete()
        Location.objects.all().delete()
        Category.objects.all().delete()


