from django.test import TestCase
from join_site.models import Target


class TargetTestCase(TestCase):
    def test_create_new_target_and_return_itself(self):
        target = Target.objects.create(
            name='Cliente 1',
            latitude=123,
            longitude=123,
        )

        self.assertEqual(target.name, 'Cliente 1')
