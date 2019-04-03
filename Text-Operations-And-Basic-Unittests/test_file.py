import unittest
import file
from math import pi

class TestFuzzBuzz(unittest.TestCase):
    def test_value(self):
        self.assertRaises(ValueError,file.FuzzBuzz,-10,-10)

    def test_types(self):
        self.assertRaises(TypeError,file.FuzzBuzz,1+2j,1+2j)
        self.assertRaises(TypeError,file.FuzzBuzz,True)
        self.assertRaises(TypeError,file.FuzzBuzz,None)
        self.assertRaises(TypeError,file.FuzzBuzz,"asd")
        self.assertRaises(TypeError,file.FuzzBuzz,[2,1,3])
        self.assertRaises(TypeError,file.FuzzBuzz,0.123)
        self.assertRaises(TypeError,file.FuzzBuzz,(123,123))
        self.assertRaises(TypeError,file.FuzzBuzz,{"fuzz":"buzz"})



class TestCircleRadious(unittest.TestCase):
    def test_area(self):
        #Test areas when rad >=0F
        self.assertAlmostEqual(file.circleRadious(1), pi)
        self.assertAlmostEqual(file.circleRadious(0), 0)
        self.assertAlmostEqual(file.circleRadious(2.1), pi*2.1**2)
    
    def test_value(self):
        self.assertRaises(ValueError, file.circleRadious, -2)

    def test_types(self):
        self.assertRaises(TypeError, file.circleRadious, 1+2j)
        self.assertRaises(TypeError, file.circleRadious, True)
        self.assertRaises(TypeError, file.circleRadious, "asd")

class TestDelta(unittest.TestCase):
    def testdelta(self):
        self.assertEqual(file.delta(2,2,2),-12)
        self.assertEqual(file.delta(1,10,1),96)

    def test_value(self):
        self.assertRaises(ValueError,file.delta,-2,-2,-2)
        
    def test_ifNull(self):
        self.assertRaises(ValueError,file.delta,None,None,None)

    def test_types(self):
        self.assertRaises(TypeError, file.delta, 1+2j)
        self.assertRaises(TypeError,file.delta,True)
        self.assertRaises(TypeError,file.delta,"asd")

if __name__ == '__main__':
        unittest.main()