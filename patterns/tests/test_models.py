from django.test import TestCase

from patterns.models import PatternCompany


# Create your tests here.
class PatternCompanyTestCase(TestCase):
    @classmethod
    def setUp(cls):
        PatternCompany.objects.create(
            company="Test Company",
            location="NYC",
            website="https://fakewebsite.com")

    def test_company_name(self):
        test_company = PatternCompany.objects.get(id=1)
        field_label = test_company._meta.get_field('company').verbose_name
        self.assertsEquals(field_label, 'company')

    def test_company_location(self):
        test_company = PatternCompany.objects.get(id=1)
        field_label = test_company._meta.get_field('location').verbose_name
        self.assertsEquals(field_label, 'location')

    def test_company_url(self):
        test_company = PatternCompany.objects.get(id=1)
        field_label = test_company._meta.get_field('website').verbose_name
        self.assertsEquals(field_label, 'website')

    def test_company_name_max_length(self):
        test_company = PatternCompany.objects.get(id=1)
        max_length = test_company._meta.get_field('company').max_length
        self.assertsEquals(max_length, 100)

    def test_company_location_max_length(self):
        test_company = PatternCompany.objects.get(id=1)
        max_length = test_company._meta.get_field('location').max_length
        self.assertsEquals(max_length, 100)
