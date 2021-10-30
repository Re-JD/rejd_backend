from django.test import TestCase
from .models import User, UserManager
from django.db.utils import IntegrityError

# Create your tests here.
class UserManagerTestCase(TestCase):
    def setUp(self):
        with self.assertRaises(TypeError) as context:
            User.objects.create_user()
        self.assertTrue("create_user() missing 1 required positional argument: 'email'" in str(context.exception))
        # with self.assertRaises(ValueError) as context:
        #     User.objects.create_user(password='123')
        # self.assertTrue('Must have an Email address' in context.exception)
        # with self.assertRaises(ValueError) as context:
        #     User.objects.create_user(email='abc@abc.com')
        # self.assertTrue('Must have password' in context.exception)
        # with self.assertRaises(ValueError) as context:
        #     User.objects.create_user(email='abcabc.com')
        # self.assertTrue('Must have password' in context.exception)

        # User.objects.create_user(email='abc1@abc.com', password='123')
    
    def test_user_creation(self):
        user1=User.objects.create_user(email='abc1@abc.com', password='123')
        self.assertEqual(user1.email, 'abc1@abc.com')
        self.assertEqual(user1.check_password('123'), True)

class UserTestCase(TestCase):
    def test_user_email_duplication_check(self):
        user1 = User.objects.create_user(email='abcd@naver.com', password='123')
        with self.assertRaises(IntegrityError) as context:
            user2 = User.objects.create_user(email='abcd@naver.com', password='456')
        
        self.assertTrue('UNIQUE constraint failed: user_auth_user.email' in str(context.exception))