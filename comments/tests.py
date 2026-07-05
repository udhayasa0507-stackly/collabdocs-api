from django.test import TestCase

from users.models import User
from workspaces.models import Workspace
from documents.models import Document
from comments.models import Comment


class CommentTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(
            first_name="Udhaya",
            last_name="Sankar",
            email="udhayasa@gmail.com",
            phone="9791972823"
        )

        self.workspace = Workspace.objects.create(
            name="Workspace",
            owner=self.user
        )

        self.document = Document.objects.create(
            title="Test",
            content="Hello",
            workspace=self.workspace,
            created_by=self.user,
            status="draft"
        )

    def test_create_comment(self):
        comment = Comment.objects.create(
            document=self.document,
            author=self.user,
            content="Nice document!"
        )

        self.assertEqual(comment.content, "Nice document!")