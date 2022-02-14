import configparser
from genericUtils import Utils

class Apartment:
    def __init__(self, members):
        self.numMembers = members
        self.usageLimit = self.numMembers * int(Utils.getAptParamValue('USAGE_LIMIT')) * int(Utils.getAptParamValue('MONTH_DAYS'))

    def __call__(self):
        return f"Apartment houses {self.numMembers} members"

class TwoBedRoomApartment(Apartment):
    def __init__(self) -> None:
        try:
            super().__init__(int(Utils.getAptParamValue('TWOBED')))
        except configparser.NoSectionError as e:
            print('Section not found :' + e.args)
        


class ThreeBedRoomApartment(Apartment):
    def __init__(self) -> None:
        try:
            super().__init__(int(Utils.getAptParamValue('THREEBED')))
        except configparser.NoSectionError as e:
            print('Section not found :' + e.args)




if __name__ == '__main__':
    try:
        a2 = TwoBedRoomApartment()
        print(a2.numMembers)
        a3 = ThreeBedRoomApartment()
        print(a3.numMembers)
    except Exception as e:
        print(e.args[0])