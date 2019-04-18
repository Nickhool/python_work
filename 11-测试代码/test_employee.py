__Author__ = "noduez"

import unittest

from employee import Employee


class TestEmployee(unittest.TestCase):
    """测试模块employee。"""

    def setUp(self):
        """创建一个Employee实例，以便在测试中使用。"""
        self.eric = Employee('eric', 'matthes', 65000)

    def test_give_default_raise(self):
        """测试使用默认的年薪增加量是否可行。"""
        self.eric.give_raise()
        self.assertEqual(self.eric.salary, 70000)

    def test_give_custom_raise(self):
        """测试自定义年薪增加量是否可行。"""
        self.eric.give_raise(10000)
        self.assertEqual(self.eric.salary, 75000)

if __name__=="__main__":
    unittest.main()