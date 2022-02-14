
import genericUtils
import configparser
import apartmentDetails


class Household(object):
    
    def __init__(self, apt_type):
        if apt_type < 1 or apt_type > 3:
            raise ValueError("Apartment type can only be 2 (2-bed) or 3 (3-bed)")
        self.ApartmentType = apt_type

        if self.ApartmentType == 2:
            self.ApartmentDetails = apartmentDetails.TwoBedRoomApartment()
        elif self.ApartmentType == 3:
            self.ApartmentDetails = apartmentDetails.ThreeBedRoomApartment()

    def __str__(self):
        return f"Apartment::Type: {self.ApartmentType}, Member: {self.ApartmentDetails.numMembers}, UsageLimit: {self.ApartmentDetails.usageLimit}"

    def __call__(self):
        return f"Apartment::Type: {self.ApartmentType}, Member: {self.ApartmentDetails.numMembers}, UsageLimit: {self.ApartmentDetails.usageLimit}"


if __name__ == '__main__':
    try:
        h1 = Household(apt_type=2)
        print(h1())
    except ValueError as e:
        print ("ERROR: " + e.args[0])

    try:
        h2 = Household(apt_type=3)
        print(h2())
    except ValueError as e:
        print ("ERROR: " + e.args[0])

    try:
        h3 = Household(apt_type=4)
        print(h3())
    except ValueError as e:
        print ("ERROR: " + e.args[0])

    try:
        h4 = Household(apt_type=0)
        print(h4())
    except ValueError as e:
        print ("ERROR: " + e.args[0])

