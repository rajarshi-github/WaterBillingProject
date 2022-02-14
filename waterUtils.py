from Household import Household
from genericUtils import Utils
from waterCharges import waterCharges
import os

class waterUtils:

    '''
        This class has all attributes and member functions to calculate total water usage and charges
    '''

    def __init__(self, usagesummary):
        '''
            usageSummary :

            This dictionary will hold the summarized command list read from the input file

                apttype = 1 or 2

                CorporationUsage = fraction used from Corporation Water (converted to decimal)

                BorewellUsage = fraction used from Borewell water (converted to decimal)

                numGuests = total number of guests in the entire month
                            can have multiple ADD_GUESTS command

                billGenerate = Generates bill if turned to True else not
                                default is False, once I get the BILL command it is turned to True

        '''
        self.usageSummary = usagesummary

    def __call__(self):
        return self.usageSummary

    def __str__(self):
        return self.usageSummary

    def calculateBoreWaterUsage(self):
        h = Household(apt_type=self.usageSummary['apttype'])
        return h.ApartmentDetails.usageLimit * self.usageSummary['BorewellUsage']
    
    def calculateBoreWaterCharges(self):
        return waterCharges.waterCharges( waterSource='bore', consumption = round( self.calculateBoreWaterUsage() ))

    def calculateCorpWaterUsage(self):
        h = Household(apt_type=self.usageSummary['apttype'])
        return h.ApartmentDetails.usageLimit * self.usageSummary['CorporationUsage']

    def calculateCorpWaterCharges(self):
        return waterCharges.waterCharges( waterSource='corp', consumption = round( self.calculateCorpWaterUsage() ))

    def calculateTankerWaterUsage(self):
        h = Household(apt_type=self.usageSummary['apttype'])
        return self.usageSummary['numGuests'] * int(Utils.getAptParamValue('USAGE_LIMIT')) * int(Utils.getAptParamValue('MONTH_DAYS'))

    def calculateTankerWaterCharges(self):    
        return  waterCharges.waterCharges( waterSource='tanker', consumption = round( self.calculateTankerWaterUsage() ))

    def calculateTotalUsage(self):
        #print('U:bore:' + str(self.calculateBoreWaterUsage()) + ', corp:' + str(self.calculateCorpWaterUsage()) + ', tanker:' + str(self.calculateTankerWaterUsage()))
        return round( self.calculateBoreWaterUsage() + self.calculateCorpWaterUsage() + self.calculateTankerWaterUsage() )
        
    def calculateTotalCost(self):
        #print ('C:bore:' + str(self.calculateBoreWaterCharges()) + ', corp:' + str(self.calculateCorpWaterCharges()) + ', tanker:' + str(self.calculateTankerWaterCharges()))
        return round(self.calculateBoreWaterCharges() + self.calculateCorpWaterCharges() + self.calculateTankerWaterCharges())



if __name__ == '__main__':
    sep = '/'
    CWD = os.getcwd() + sep

    file = CWD + 'test1.txt'    
    t1 = Utils.readInput(file)
    w1 = waterUtils(t1)        
    #print(w1())
    print( w1.calculateTotalCost(),  w1.calculateTotalUsage())

    file = CWD + 'test2.txt'    
    t1 = Utils.readInput(file)
    w1 = waterUtils(t1)        
    #print(w1())
    print( w1.calculateTotalCost(),  w1.calculateTotalUsage())


    file = CWD + 'test3.txt'    
    t1 = Utils.readInput(file)
    w1 = waterUtils(t1)        
    #print(w1())
    print( w1.calculateTotalCost(),  w1.calculateTotalUsage())
