from django.core.exceptions import ValidationError
from django.test import TestCase

from donations.models.ngos import ngo_slug_validator


class NgoSlugValidatorTests(TestCase):
    def setUp(self):
        self.valid_slugs = (
            "abc",
            "my-ngo",
            "asociatia-mea",
            "a1b2",
            "abc-def-ghi",
        )

        self.invalid_slugs = (
            # uppercase characters are not allowed
            "ABC",
            "MyNgo",
            # characters that are neither lowercase alphanumeric nor a hyphen
            "ab_cd",
            "ab cd",
            "ab.cd",
            "ab!cd",
            # digit-only / hyphen-only values have no cased characters, so
            # they are rejected before the charset check even runs
            "123",
            "---",
            # empty value
            "",
        )

    def test_valid_slugs_pass(self):
        for slug in self.valid_slugs:
            self.assertEqual(ngo_slug_validator(slug), None)

    def test_invalid_slugs_are_rejected(self):
        for slug in self.invalid_slugs:
            self.assertRaises(ValidationError, ngo_slug_validator, slug)
