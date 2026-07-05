from django.test import TestCase

from users.models import User
from workspaces.models import Workspace
from documents.models import Document, DocumentVersion


class DocumentTest(TestCase):

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

    def test_create_document(self):
        document = Document.objects.create(
            title="My First Doc",
            content="Hello Airtribe",
            workspace=self.workspace,
            created_by=self.user,
            status="draft"
        )

        self.assertEqual(document.title, "My First Doc")

    def test_create_document_version(self):
        document = Document.objects.create(
            title="Version Test",
            content="Version 1",
            workspace=self.workspace,
            created_by=self.user,
            status="draft"
        )

        version = DocumentVersion.objects.create(
            document=document,
            version_number=1,
            content=document.content,
            saved_by=self.user
        )

        self.assertEqual(version.version_number, 1)