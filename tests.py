import unittest
import re
from parameterized import parameterized
from regex import sprawdz

pattern = re.compile(r'^ab(a|b)*(a|b)$')

class TestProject1(unittest.TestCase):

    @parameterized.expand([
        '010101',
        '010100',
        "101000",
        '0000000000000',
        '10bf101010',
        '010101001',
        '0101010101'
        '1010101010'
        '1111'
        '/fdsrq23'
        'abdddeeee'
        '10000100'
        '15'
        'xtz'
        'basia'
        'asia'
        '1011'

    ])
    def test_isAccepted(self, ciag):
        wynik = 'A' if re.match(pattern, ciag) else 'N'
        self.assertEqual(wynik, sprawdz(ciag), "Ciag: " + ciag)
