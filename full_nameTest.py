import unittest
import full_name


class MyTestCase(unittest.TestCase):
    def test_normal(self):
        self.assertEqual(full_name.full_name('Астрейко','Татьяна','Михайловна'), 'Астрейко Татьяна Михайловна')

    def test_big(self):
        self.assertEqual(full_name.full_name('АСТРЕЙКО','ТАТЬЯНА','МИХАЙЛОВНА'), 'Астрейко Татьяна Михайловна')

    def test_small(self):
        self.assertEqual(full_name.full_name('астрейко','татьяна','михайловна'), 'Астрейко Татьяна Михайловна')
