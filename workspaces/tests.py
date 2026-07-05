from django.test import TestCase

from users.models import User
from workspaces.models import Workspace


class WorkspaceTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(
            first_name="Udhaya",
            last_name="Sankar",
            email="udhayasa0507@gmail.com",
            phone="9791972823"
        )

    def test_create_workspace(self):
        workspace = Workspace.objects.create(
            name="Airtribe Workspace",
            owner=self.user
        )

        self.assertEqual(workspace.name, "Airtribe Workspace")
        self.assertEqual(workspace.owner, self.user)