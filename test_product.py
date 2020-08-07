import unittest 

from product import Product

class ProductTestCase(unittest.TestCase):
    def test_generate_sku(self):
        small_shoes = Product('shoes', 'S', 'black')
        self.assertEqual(small_shoes.generate_sku(), 'SHOES-S-BLACK')


if __name__ == '__main__':
    unittest.main()