
import configparser
import os


class Utils:

    @classmethod
    def getAptParamValue(self, param):
        '''
            Reads the ini file parameters
        '''
        conf = configparser.ConfigParser()
        conf.read('household.ini')
        #conf.get('apartment', param)
        return conf.get('apartment', param)


    @classmethod
    def readInput(self, filename):
        '''
            Reads the input file (testcase)
        '''
        try:
            aptType = 0
            numGuests = 0
            CorporationUsage = 0.0
            BorewellUsage = 0.0
            billGeneration = False

            with open(filename, 'r') as f:

                for idx, line in enumerate(f.readlines()):

                    functionName = line.strip().split()[0]

                    if (idx == 0) and (functionName != 'ALLOT_WATER'):
                        raise ValueError("Expecting ALLOT_WATER details in the 1st row in input")
                        
                    if idx == 0:
                            aptType = int(line.strip().split()[1])

                            waterAllotRatio = line.strip().split()[2]

                            corp = int(waterAllotRatio.split(':')[0])
                            bore = int(waterAllotRatio.split(':')[1])

                            CorporationUsage = corp / (corp + bore)
                            BorewellUsage = bore / (corp + bore)

                    else:
                        if functionName == 'ADD_GUESTS':
                            numGuests += int(line.strip().split()[1])

                        if functionName == 'BILL':
                            billGeneration = True

            return  {   'apttype':aptType, 
                        'CorporationUsage':CorporationUsage, 
                        'BorewellUsage':BorewellUsage, 
                        'numGuests':numGuests, 
                        'billGeneration':billGeneration
                    }
            
            return waterUtility

        except Exception as e2:
            raise FileNotFoundError



if __name__ == '__main__':
    sep = '/'
    CWD = os.getcwd() + sep

    try:

        print(Utils.getAptParamValue('TWOBED'))
        print(Utils.getAptParamValue('THREEBED'))
        print(Utils.getAptParamValue('USAGE_LIMIT'))

        file = CWD + 'test1.txt'    
        t1 = Utils.readInput(file)
        print(str(t1))


        file = CWD + 'test2.txt'    
        t2 = Utils.readInput(file)
        print(t2)

        file = CWD + 'test3.txt'    
        t3 = Utils.readInput(file)
        print(t3)

        file = CWD + 'test4.txt'    
        #t4 = Utils.readInput(file)
        #print(t4)

    except Exception as e:
        print('ERROR : ' + e.args[0])