from django.test import TestCase

# Create your tests here.

from django.test import TestCase

from .models import Image,Category,Location
import datetime as dt

# Create your tests here.
class ImageTestClass(TestCase):
    def setUp(self):
        self.location = Location(place='Eldoret')
        self.location.save_location()

        self.category = Category(category='Fruits')
        self.category.save_category()

        self.initial_test= Image(name = 'home', image='isaac.png', description='the image is in good condition',size='320px by 210px',pub_date='25-11-2021',location=self.location,category=self.category)
# Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.initial_test,Image))

    # Testing the saved methods
    def test_saved_method(self):
        self.initial_test.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)



    def test_delete_image(self):
        self.initial_test.delete_image()
        images = Image.objects.all()
        self.assertTrue(len(images)==0)

    def test_update_image(self):
        self.initial_test.save_image()
        self.initial_test.update_image(self.initial_test.id, 'images/test.jpg')
        new_image = Image.objects.filter(image='images/test.jpg')
        self.assertTrue(len(new_image)>0)

    def test_search_by_location(self):
        self.initial_test.save_image()
        images = self.initial_test.search_by_location(search_term='Eldoret')
        self.assertTrue(len(images) ==0)

    def test_search_by_category(self):
        self.initial_test.save_image()
        images = self.initial_test.search_by_category(search_term='Fruits')
        self.assertTrue(len(images)== 0)

    def tearDown(self):
        Image.objects.all().delete()
        Location.objects.all().delete()
        Category.objects.all().delete()

class CategoryTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.category = Category(category='Fruits')
        self.category.save_category()

    def test_instance(self):
        self.assertTrue(isinstance(self.category, Category))

    def test_save_category(self):
        self.category.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)

    def test_delete_category(self):
        self.category.delete_category()
        category = Category.objects.all()
        self.assertTrue(len(category) == 0)


   
    
class LocationTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.location = Location(place='Eldoret')
        self.location.save_location()

    def test_instance(self):
        self.assertTrue(isinstance(self.location, Location))

    def test_save_location(self):
        self.location.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)

    def test_delete_location(self):
        self.location.delete_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) == 0)

    def test_get_locations(self):
        self.location.save_location()
        locations = Location.get_locations()
        self.assertTrue(len(locations) > 0)


