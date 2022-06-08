from django.test import TestCase

# Create your tests here.

from django.test import TestCase

from .models import *

# Create your tests here.
class ImageTestClass(TestCase):
    def setUp(self):
        self.profile = Profile(fullname='isaac kiptoo',profile_img='isaac.png',bio='am i a tm',email_phone='isaac@gmail')
        self.profile.save_profile()

#  img_name=models.CharField(max_length=100)
#     image=models.ImageField(upload_to='image/',null=True)
#     image_caption=models.CharField(max_length=200)
#     profile=models.ForeignKey(User, on_delete = models.CASCADE)
#     likes=models.ManyToManyField(User,related_name='likes')
#     created_at=models.DateTimeField(auto_now_add=True)
    

        self.comment = Comment(category='Fruits')
        self.comment.save_comment()

        self.initial_test= Image(img_name='isaac.png',image='isaac.png',user='isaac',name = 'home',  description='the image is in good condition',size='320px by 210px',pub_date='25-11-2021',profile=self.profile,comment=self.comment)
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

    def test_search_by_name(self):
        self.initial_test.save_image()
        images = self.initial_test.search_by_name(search_term='isaac')
        self.assertTrue(len(images) ==0)

    # def test_search_by_category(self):
    #     self.initial_test.save_image()
    #     images = self.initial_test.search_by_category(search_term='Fruits')
    #     self.assertTrue(len(images)== 0)

    def tearDown(self):
        Image.objects.all().delete()
        Profile.objects.all().delete()
        Comment.objects.all().delete()

class CommentestClass(TestCase):

    # Set up method
    def setUp(self):
        self.comment = comment=('Fruits')
        self.comment.save_comment()

    def test_instance(self):
        self.assertTrue(isinstance(self.comment, Comment))

    def test_save_comment(self):
        self.comment.save_comment()
        comments = Comment.objects.all()
        self.assertTrue(len(comments) > 0)

    def test_delete_comment(self):
        self.comment.delete_comment()
        comment = Comment.objects.all()
        self.assertTrue(len(comment) == 0)


   
    
class ProfileTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.profile = Profile(place='Eldoret')
        self.profile.save_profile()

    def test_instance(self):
        self.assertTrue(isinstance(self.profile, Profile))

    def test_save_profile(self):
        self.profile.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)

    def test_delete_profile(self):
        self.profile.delete_profile()
        profiless = Profile.objects.all()
        self.assertTrue(len(profiless) == 0)

    # def test_get_locations(self):
    #     self.location.save_location()
    #     locations = Location.get_locations()
    #     self.assertTrue(len(locations) > 0)


