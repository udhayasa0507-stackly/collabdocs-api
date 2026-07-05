from django.test import TestCase
from users.models import User

class UserModelTest(TestCase):

    def test_create_user(self):
        user = User.objects.create(
            first_name="Udhaya",
            last_name="Sankar",
            email="udhayasa0507@gmail.com",
            phone="9791972823"
        )

        self.assertEqual(user.first_name, "Udhaya")
        self.assertEqual(user.email, "udhayasa0507@gmail.com")