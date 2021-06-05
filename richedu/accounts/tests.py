from .views import users_delete
from django.urls.base import resolve
from .models import CustomUser
from django.test import TestCase
from django.urls import reverse
# Create your tests here.

from django.contrib.auth import get_user_model
from django.test import TestCase


class UsersManagersTests(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(email='normal@user.com', password='foo')
        self.assertEqual(user.email, 'normal@user.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        try:
            # username is None for the AbstractUser option
            # username does not exist for the AbstractBaseUser option
            self.assertIsNone(user.username)
        except AttributeError:
            pass
        with self.assertRaises(TypeError):
            User.objects.create_user()
        with self.assertRaises(TypeError):
            User.objects.create_user(email='')
        with self.assertRaises(ValueError):
            User.objects.create_user(email='', password="foo")

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(email='super@user.com', password='foo')
        self.assertEqual(admin_user.email, 'super@user.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        try:
            # username is None for the AbstractUser option
            # username does not exist for the AbstractBaseUser option
            self.assertIsNone(admin_user.username)
        except AttributeError:
            pass
        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                email='super@user.com', password='foo', is_superuser=False)
    
    def test_create_superuser_is_staff(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(email='super@user.com', password='foo')
        self.assertEqual(admin_user.email, 'super@user.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        try:
            # username is None for the AbstractUser option
            # username does not exist for the AbstractBaseUser option
            self.assertIsNone(admin_user.username)
        except AttributeError:
            pass
        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                email='super@user.com', password='foo', is_staff=False)
        
    def test_user_name(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(email='super@user.com', password='foo')
        self.assertEqual(admin_user.email, 'super@user.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        self.assertEquals(str(admin_user),'super@user.com')
    
    def test_user(self):
        admin_user = CustomUser.objects.create(email='super@user.com', password='foo',name='shah')
        self.assertEqual(admin_user.email, 'super@user.com')
        self.assertTrue(admin_user.is_active)
        
    
class BaseTest(TestCase):
    def setUp(self):
        self.create_url = reverse('users')
        self.list_url=reverse('users')
        self.user={
            'email':'testemail@gmail.com',
            'name':'test',
            'password':'password',
        }
        return super().setUp()

class CreateTest(BaseTest):
    def test_can_register_user(self):
        response=self.client.post(self.create_url,self.user,format='text/html')
        self.assertEqual(response.status_code,302)
    
    def test_can_list_user(self):
        response=self.client.get(self.list_url,format='text/html')
        self.assertEqual(response.status_code,200)
    
    def test_can_delete_user(self):
        admin_user = CustomUser.objects.create(email='super@user.com', password='foo',name='shah')
        url = reverse('users_delete', args=["1"])
        response=self.client.post(url)
        self.assertEqual(response.status_code,302)
    
    def test_can_edit_user(self):
        admin_user = CustomUser.objects.create(email='super@user.com', password='foo',name='shah')
        url = reverse('users_edit', args=["1"])
        response=self.client.post(url,{'name':'don'})
        self.assertEqual(response.status_code,302)
    
    def test_can_get_edit_user(self):
        admin_user = CustomUser.objects.create(email='super@user.com', password='foo',name='shah')
        url = reverse('users_edit', args=["1"])
        response=self.client.get(url)
        self.assertEqual(response.status_code,200)
        
    