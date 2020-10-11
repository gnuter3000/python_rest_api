from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """test creating a new user with an email successful"""
        email = 'test@email.de'
        password = 'testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_user_email_normalized(self):
        """test the email for a new user is normalized"""
        email = 'test2@EmaiL.DE'
        user = get_user_model().objects.create_user(
            email=email,
            password='123123123'
        )

        self.assertEqual(user.email, email.lower())

    def test_new_user_email_invalid(self):
        """test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, '123')

    def test_create_new_superuser(self):
        """Test creating a superuser"""
        user = get_user_model().objects.create_superuser(
            'superuser@email.com', '123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
