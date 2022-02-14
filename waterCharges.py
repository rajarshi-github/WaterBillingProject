import configparser

class waterCharges:

    @classmethod
    def getCorpRateSlab(self):
        conf = configparser.ConfigParser()
        conf.read('waterRates.ini')
        return  [{ int(conf.get('corporation', 'SLAB1_START')) : float(conf.get('corporation', 'SLAB1_RATE')) }]

    @classmethod
    def getBoreRateSlab(self):
        conf = configparser.ConfigParser()
        conf.read('waterRates.ini')
        return  [{ int(conf.get('borewell', 'SLAB1_START')) : float(conf.get('borewell', 'SLAB1_RATE')) }]

    @classmethod
    def getTankerRateSlab(self):
        conf = configparser.ConfigParser()
        conf.read('waterRates.ini')
        
        l = [
                {int(conf.get('tanker', 'SLAB1_START')) : float(conf.get('tanker', 'SLAB1_RATE')) },
                {int(conf.get('tanker', 'SLAB2_START')) : float(conf.get('tanker', 'SLAB2_RATE')) }, 
                {int(conf.get('tanker', 'SLAB3_START')) : float(conf.get('tanker', 'SLAB3_RATE')) }, 
                {int(conf.get('tanker', 'SLAB4_START')) : float(conf.get('tanker', 'SLAB4_RATE')) } 
            ]
        return l

    @classmethod
    def cumulativeSlabsRates(self, lstSlabs, consumption):
        totalCharges = 0    

        for slab in lstSlabs[::-1]:
            [(slabStart, slabRate)] = slab.items()

            if consumption > slabStart:
                totalCharges += (consumption - slabStart) * slabRate
                consumption = slabStart

        return totalCharges        



    @classmethod
    def waterCharges(self, waterSource='bore', consumption=0):

        if waterSource == 'bore':
            rateSlab = waterCharges.getBoreRateSlab()

        if waterSource == 'corp':
            rateSlab = waterCharges.getCorpRateSlab()
        
        if waterSource == 'tanker':
            rateSlab = waterCharges.getTankerRateSlab()


        totalCharges = waterCharges.cumulativeSlabsRates(rateSlab, consumption)
        return totalCharges





        
    
