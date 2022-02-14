
import sys
from waterUtils import waterUtils
from genericUtils import Utils


def main():
    file = sys.argv[1]
    t1 = Utils.readInput(file)
    w1 = waterUtils(t1)        
    print( w1.calculateTotalUsage(), w1.calculateTotalCost()  )

def testrun(file):
    t1 = Utils.readInput(file)
    w1 = waterUtils(t1)        
    print( w1.calculateTotalUsage(), w1.calculateTotalCost())
    

if __name__ == '__main__':
    main()


