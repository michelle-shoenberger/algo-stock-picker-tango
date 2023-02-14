
from stock_picker import picker
import unittest

class StockPickerTest(unittest.TestCase):
#   def test_return(self):
#     """test return of function"""
#     self.assertIsNotNone(picker([1,"2",4]))
    
  def test_simple_1(self):
    """simple test case"""
    self.assertEqual(picker([1,2,3,4]), [0,3])

  def test_simple_2(self):
    """simple test case"""
    self.assertEqual(picker([17,3,6,9,15,8,6,1,10]), [1,4])

  def test_simple_3(self):
    """simple test case"""
    self.assertEqual(picker([3,17,6,9,18,15,6,1,10]), [0,4])

  def test_simple_4(self):
    """simple test case"""
    self.assertEqual(picker([1,17,6,9,8,15,6,3,19]), [0,8])

  def test_simple_5(self):
    """simple test case"""
    self.assertEqual(picker([19,17,6,9,8,15,6,3,1]), [2,5])

if __name__ == "__main__":
  unittest.main()

# print(picker([17,3,6,9,15,8,6,1,10]) == [1,4])
# print(picker([3,17,6,9,18,15,6,1,10]) == [0,4])
# print(picker([1,17,6,9,8,15,6,3,19]) == [0,8])
# print(picker([19,17,6,9,8,15,6,3,1]) == [2,5])