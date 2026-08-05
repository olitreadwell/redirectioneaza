from django.core.exceptions import ValidationError
from django.test import TestCase

from utils.validators import url_validator


class UrlValidatorTests(TestCase):
    def setUp(self):
        self.valid_subdomains = (
            "abc",
            "my-ngo",
            "asociatia-mea",
            "a1b2",
            "abc-def-ghi",
            "x" * 100,
        )

        self.reserved_subdomains = (
            "redirectioneaza",
            "www",
            "admin",
            "api",
            "ftp",
            "dns",
            "ns1",
            "ns2",
        )

        self.invalid_subdomains = (
            # uppercase characters are not allowed
            "ABC",
            "MyNgo",
            # too short (fewer than 3 characters)
            "ab",
            # too long (more than 100 characters)
            "x" * 101,
            # characters that are neither alphanumeric nor a hyphen
            "ab_cd",
            "ab cd",
            "ab.cd",
            "ab!cd",
            # only hyphens, nothing alphanumeric left
            "--",
            # empty value
            "",
        )

    def test_valid_subdomains_pass(self):
        for subdomain in self.valid_subdomains:
            self.assertEqual(url_validator(subdomain), None)

    def test_reserved_subdomains_are_rejected(self):
        for subdomain in self.reserved_subdomains:
            self.assertRaises(ValidationError, url_validator, subdomain)

    def test_invalid_subdomains_are_rejected(self):
        for subdomain in self.invalid_subdomains:
            self.assertRaises(ValidationError, url_validator, subdomain)
