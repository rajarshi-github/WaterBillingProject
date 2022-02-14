import unittest
import geektrust

from waterUtils import waterUtils
from genericUtils import Utils
from Household import Household
from apartmentDetails import TwoBedRoomApartment, ThreeBedRoomApartment

class TestGeekTrust(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print('Testing geektrust ... ')
    
    @classmethod
    def tearDownClass(cls) -> None:
        print('Testing Completed')

    def setUp(self) -> None:
        return super().setUp()

    def tearDown(self) -> None:
        return super().tearDown()

    def test_main(self):
        print("main")
        with self.assertRaises(FileNotFoundError):
            geektrust.testrun(file='test8.txt')
    
    def test_waterUtils_1(self):
        t1 = Utils.readInput('test1.txt')
        w1 = waterUtils(t1)        
        self.assertEqual( str(w1.calculateTotalCost()), '5215')

    def test_waterUtils_2(self):
        t1 = Utils.readInput('test1.txt')
        w1 = waterUtils(t1)        
        self.assertEqual( str(w1.calculateTotalUsage()), '2400')

    def test_waterUtils_3(self):
        t1 = Utils.readInput('test2.txt')
        w1 = waterUtils(t1)        
        self.assertEqual( str(w1.calculateTotalCost()), '5750')

    def test_waterUtils_4(self):
        t1 = Utils.readInput('test2.txt')
        w1 = waterUtils(t1)        
        self.assertEqual( str(w1.calculateTotalUsage()), '3000')

    def test_waterUtils_5(self):
        t1 = Utils.readInput('test3.txt')
        w1 = waterUtils(t1)        
        self.assertEqual( str(w1.calculateTotalCost()), '1200')

    def test_waterUtils_6(self):
        t1 = Utils.readInput('test3.txt')
        w1 = waterUtils(t1)        
        self.assertEqual( str(w1.calculateTotalUsage()), '900')

    def test_genericUtils_1(self):
        self.assertEqual(str(Utils.getAptParamValue('TWOBED')), '3')

    def test_genericUtils_2(self):
        self.assertEqual(str(Utils.getAptParamValue('THREEBED')), '5')

    def test_genericUtils_3(self):
        self.assertEqual(str(Utils.getAptParamValue('USAGE_LIMIT')), '10')

    def test_genericUtils_4(self):
        t1 = Utils.readInput('test1.txt')
        self.assertEqual(str(t1), '{\'apttype\': 2, \'CorporationUsage\': 0.3, \'BorewellUsage\': 0.7, \'numGuests\': 5, \'billGeneration\': True}')

    def test_genericUtils_5(self):
        t1 = Utils.readInput('test2.txt')
        self.assertEqual(str(t1), '{\'apttype\': 3, \'CorporationUsage\': 0.6666666666666666, \'BorewellUsage\': 0.3333333333333333, \'numGuests\': 5, \'billGeneration\': True}')

    def test_Household_1(self):
        h1 = Household(apt_type=2)
        self.assertEqual(str(h1()), 'Apartment::Type: 2, Member: 3, UsageLimit: 900')

    def test_Household_2(self):
        h1 = Household(apt_type=3)
        self.assertEqual(str(h1()), 'Apartment::Type: 3, Member: 5, UsageLimit: 1500')

    def test_Household_3(self):
        with self.assertRaises(ValueError):
            Household(apt_type=5)

    def test_Household_4(self):
        with self.assertRaises(ValueError):
            Household(apt_type=0)

    def test_Household_5(self):
        with self.assertRaises(ValueError):
            Household(apt_type=4)

    def test_apartmentDetails_1(self):
        a1 = TwoBedRoomApartment()
        self.assertEqual(str(a1()), 'Apartment houses 3 members')

    def test_apartmentDetails_1(self):
        a1 = ThreeBedRoomApartment()
        self.assertEqual(str(a1()), 'Apartment houses 5 members')


if __name__ == '__main__':
    unittest.main()

