from django.test import TestCase

from tags.models import Tag


class TagTest(TestCase):

    def test_create_tag(self):
        tag = Tag.objects.create(
            name="Backend"
        )

        self.assertEqual(tag.name, "Backend")