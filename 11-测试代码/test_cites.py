__Author__ = "noduez"

import unittest

from city_functions import city_country
from city_functions import city_country_population


class CitesTestCase(unittest.TestCase):

    # 11-1国家和城市
    def test_city_country(self):
        """传入简单的城市和国家可行吗？"""
        santiago_chile = city_country('santiago', 'chile')
        self.assertEqual(santiago_chile, 'Santiago, Chile')

    # 11-2人口数量
    def test_city_country_population(self):
        """可向形参population传递值吗？"""
        santiago_chile = city_country_population('santiago', 'chile', population=5000000)
        self.assertEqual(santiago_chile, 'Santiago, Chile - population 5000000')

if __name__=="__main__":
    unittest.main()